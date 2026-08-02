from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chatbot_service import chatbot_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):
    return chatbot_response(request.message)