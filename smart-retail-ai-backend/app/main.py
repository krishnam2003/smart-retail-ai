from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    product,
    sentiment,
    chatbot,
    face
)

app = FastAPI(
    title="SmartRetailAI API",
    version="1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product.router)
app.include_router(sentiment.router)
app.include_router(chatbot.router)
app.include_router(face.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to SmartRetailAI API"
    }