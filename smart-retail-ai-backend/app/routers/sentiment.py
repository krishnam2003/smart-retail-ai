from fastapi import APIRouter
from pydantic import BaseModel

from app.services.sentiment_service import analyze_sentiment

router = APIRouter()

class ReviewRequest(BaseModel):
    review: str

@router.post("/analyze-review")
def analyze(request: ReviewRequest):
    return analyze_sentiment(request.review)