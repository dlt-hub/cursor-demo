### Steps

1. Enable [ long context chat ]( https://docs.cursor.com/chat/overview#long-context-chat-beta ) so you can use most of dlt codebase and documentation as context.
2. Cursor.ai's embeddings search works on small codebases, but given the complexity of dlt code, it's better to use the `@codebase` command to rerank and reason more about the best answer. This will consume credits though.


### Workflow

1) First describe in detail in the [chat modal](https://docs.cursor.com/chat/overview) `Cmd L` what you would like to accomplish.
2) If the pipeline works, great! If not, edit the problematic code pieces using the [inline AI chat](https://docs.cursor.com/cmdk/overview) `Cmd K`.