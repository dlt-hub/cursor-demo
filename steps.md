### Steps to Enable a Great dlt+cursor Development Experience

1. Set your "rules for ai" to use the accompanyijng `.cursorfiles`: ![](assets/cursor-file.png)

2. Index the dlt documentation:![](assets/index.png)

2. Enable [ long context chat ]( https://docs.cursor.com/chat/overview#long-context-chat-beta ), which uses Claude 200k, so you can use most of dlt codebase and documentation as context:
![](assets/long-context.png)

3. Add the dlt docs to the knowleadge base with the [@Docs](https://docs.cursor.com/context/@-symbols/@-docs) symbol:![](assets/docs-sym.png)

4. Cursor.ai's embeddings search works on small codebases, but given the complexity of dlt code, it's better to use the `@codebase` command to rerank and reason more about the best answer. This will consume credits though. Be sure to select **Reranker as "smart"** and **Reasoning step as "yes"**.  ![](assets/reranker.png)

5. Describe *in detail* in the [chat modal](https://docs.cursor.com/chat/overview) `Cmd L` what you would like to accomplish. Be sure to set the modes as described above. Finally send the RAG pipeline to run with by hitting `ctrl+⏎` (Full codebase scan + super smart reranker + reasoning). :![](assets/send-message.png)


6. If the pipeline works, great! If not, edit the problematic code pieces using the [inline AI chat](https://docs.cursor.com/cmdk/overview) `Cmd K`.