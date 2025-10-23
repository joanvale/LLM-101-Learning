from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()
sentiment_analyzer = pipeline("sentiment-analysis")

@router.post("/analyze")
async def analyze_sentiment(request: SentimentAnalysisRequest):
    try:
        result = sentiment_analyzer(request.text)[0]
        return {
            "label": result["label"], 
            "confidence": round(result["score"], 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
