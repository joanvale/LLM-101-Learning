from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@router.post("/summarize")
async def summarize(request: SummarizationRequest):
    try:
        summary = summarizer(request.text, max_length=50, min_length=10, do_sample=False)
        return {"summarized_text": summary[0]["summary_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
