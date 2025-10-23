from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter()
generator = pipeline("text-generation", model="gpt2")

@router.post("/generate-text")
async def generate_text(request: TextGeneration):
    try:
        result = generator(request.prompt, max_length=100, num_return_sequences=1)
        return {"generated_text": result[0]["generated_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
