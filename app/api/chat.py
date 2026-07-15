from pathlib import Path

from fastapi import APIRouter

from app.models.chat import ChatRequest
from app.services.bedrock import chat_with_bedrock
from app.services.chunker import chunk_text
from app.services.embeddings import generate_embedding
from app.services.parser import extract_text_from_pdf
from app.services.prompt_builder import build_prompt
from app.services.retriever import Retriever
from app.services.vector_store import VectorStore

router = APIRouter()


def load_sample_documents() -> VectorStore:
    """
    Load the local sample PDF into the in-memory vector store so
    retrieval can answer from that document during chat requests.
    """
    store = VectorStore()

    sample_pdf = Path(__file__).resolve().parents[2] / "sample.pdf"
    if not sample_pdf.exists():
        return store

    text = extract_text_from_pdf(str(sample_pdf))
    if not text.strip():
        return store

    for chunk in chunk_text(text, chunk_size=300, overlap=50):
        embedding = generate_embedding(chunk)
        store.add(embedding, chunk)

    return store


# Create objects only once
vector_store = load_sample_documents()
retriever = Retriever(vector_store)


@router.post("/chat")
def chat(request: ChatRequest):
    # Step 1: Get relevant chunks
    context = retriever.retrieve(request.question)

    # Step 2: Build the prompt
    prompt = build_prompt(context, request.question)

    # Step 3: Send prompt to Bedrock
    answer = chat_with_bedrock(prompt)

    return {
        "question": request.question,
        "answer": answer
    }