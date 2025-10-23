# schemas.py

from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    message: str

class GeneratedText(BaseModel):
    prompt: str

class TranslationInput(BaseModel):
    text: str
    target_language: str

class SummaryRequest(BaseModel):
    text: str

class SentimentRequest(BaseModel):
    text: str


