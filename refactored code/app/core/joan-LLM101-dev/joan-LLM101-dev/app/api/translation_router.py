from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from deep_translator import GoogleTranslator
import logging

router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.post("/translate")
def translate_text(request: TranslationRequest):
    try:
        translator = GoogleTranslator(source="auto", target=request.target_language)
        translated_text = translator.translate(request.text)
        return {"translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
