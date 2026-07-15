def build_prompt(context: list[str], question: str) -> str:
    """
    Build a RAG prompt using retrieved document chunks.
    """

    context_text = "\n\n".join(context)

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context, reply with:

"I couldn't find the answer in the uploaded documents."

Context:
{context_text}

Question:
{question}

Answer:
"""

    return prompt