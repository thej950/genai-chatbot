from app.services.chunker import chunk_text

text = """
Python is a programming language.

FastAPI is used to build APIs.

Amazon Bedrock provides foundation models.

RAG improves responses using documents.
"""

chunks = chunk_text(text, chunk_size=50, overlap=10)

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}")
    print(chunk)
    print("-" * 30)