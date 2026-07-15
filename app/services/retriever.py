from fastapi import APIRouter
from app.models.chat import ChatRequest
from app.services.bedrock import chat_with_bedrock
from app.services.retriever import Retriever
from app.services.vector_store import VectorStore
from app.services.prompt_builder import build_prompt

router = APIRouter()

# Create objects only once
vector_store = VectorStore()
retriever = Retriever(vector_store)

@router.post("/chat")
def chat(request: ChatRequest):

    # Retrieve relevant chunks
    context = retriever.retrieve(request.question)

    # Build prompt
    prompt = build_prompt(context, request.question)

    # Get answer from Bedrock
    answer = chat_with_bedrock(prompt)

    return {
        "question": request.question,
        "answer": answer
    }