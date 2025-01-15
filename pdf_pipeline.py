import os
import dlt
from dlt.destinations.adapters import weaviate_adapter
from PyPDF2 import PdfReader

@dlt.resource(selected=False)
def list_files(folder_path: str):
    folder_path = os.path.abspath(folder_path)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        yield {
            "file_name": filename,
            "file_path": file_path,
            "mtime": os.path.getmtime(file_path),
        }

@dlt.transformer(primary_key="page_id", write_disposition="merge")
def pdf_to_text(file_item, separate_pages: bool = False):
    if not separate_pages:
        raise NotImplementedError()
    # extract data from PDF page by page
    reader = PdfReader(file_item["file_path"])
    for page_no in range(len(reader.pages)):
        # add page content to file item
        page_item = dict(file_item)
        page_item["text"] = reader.pages[page_no].extract_text()
        page_item["page_id"] = file_item["file_name"] + "_" + str(page_no)
        yield page_item

if __name__ == "__main__":
    pipeline = dlt.pipeline(pipeline_name="pdf_to_text", destination="weaviate")

    # this constructs a simple pipeline that: 
    # (1) reads files from "pdfs" folder 
    # (2) filters only those ending with ".pdf"
    # (3) sends them to pdf_to_text transformer with pipe (|) operator
    pdf_pipeline = list_files("pdfs").add_filter(
        lambda item: item["file_name"].endswith(".pdf")
    ) | pdf_to_text(separate_pages=True)

    # set the name of the destination table to receive pages
    pdf_pipeline.table_name = "PDFText"

    # use weaviate_adapter to tell destination to vectorize "text" column
    load_info = pipeline.run(weaviate_adapter(pdf_pipeline, vectorize="text"))
    print("Load info:", load_info)

    # Query the results
    import weaviate
    client = weaviate.Client("http://localhost:8080")
    result = client.query.get("PDFText", ["text", "file_name", "mtime", "page_id"]).do()
    print("\nLoaded documents:", result)