from fastapi import APIRouter
from app.models.chat import ChatRequest
from app.services.bedrock import chat_with_bedrock

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    answer = chat_with_bedrock(request.question)

    return {
        "question": request.question,
        "answer": answer
    }