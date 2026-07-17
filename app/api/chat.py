from fastapi import APIRouter
from app.models.chat import ChatRequest
from app.services.bedrock import chat_with_bedrock
from app.services.prompt_builder import build_prompt
from app.services.retriever import Retriever
from app.services.vector_store import VectorStore

router = APIRouter()

# Create objects only once
vector_store = VectorStore()
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