from app.services.embeddings import generate_embedding
from app.services.vector_store import VectorStore


class Retriever:
    """
    Retrieve the most relevant document chunks for a user question.
    """

    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def retrieve(self, question: str, k: int = 3):
        question_embedding = generate_embedding(question)
        return self.vector_store.search(question_embedding, k=k)


def retrieve(question: str, vector_store: VectorStore | None = None, k: int = 3):
    """
    Convenience wrapper for a single retrieval call.
    """
    if vector_store is None:
        vector_store = VectorStore()

    retriever = Retriever(vector_store)
    return retriever.retrieve(question, k=k)