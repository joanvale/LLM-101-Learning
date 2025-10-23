from fastapi import FastAPI, Request, Form,  HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from transformers import pipeline
from deep_translator import GoogleTranslator
import logging
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# CORS Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

logging.basicConfig(level=logging.INFO)

# Mount static files (like CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class ChatbotRequest(BaseModel):
    message: str

class TextGeneration(BaseModel):
    prompt: str

class TranslationRequest(BaseModel):
    text: str
    target_language: str

class SummarizationRequest(BaseModel):
    text: str

class SentimentAnalysisRequest(BaseModel):
    text: str

# Initialize ChatterBot
chatbot = ChatBot("ConversationalBot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

@app.post("/chatbot/")
async def chatbot_endpoint(data: ChatbotRequest):
    user_message = data.message.strip().lower()
    
    if "hello" in user_message:
        return JSONResponse({"response": "Hello! How can I assist you today?"})
    elif "help" in user_message:
        return JSONResponse({"response": "Sure! What do you need help with?"})
    else:
        response = chatbot.get_response(user_message)
        return JSONResponse({"response": str(response)})

# Load GPT-2 model
generator = pipeline("text-generation", model="gpt2")

@app.post("/generate-text")
async def generate_text(request: TextGeneration):
    try:
        result = generator(request.prompt, max_length=100, num_return_sequences=1)
        return {"generated_text": result[0]["generated_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/translate")
def translate_text(request: TranslationRequest):
    try:
        logging.info(f"Received text: {request.text}, Target Language: {request.target_language}")
        translator = GoogleTranslator(source="auto", target=request.target_language)
        translated_text = translator.translate(request.text)
        logging.info(f"Translated text: {translated_text}")
        return {"translated_text": translated_text}
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Load the summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.post("/summarize")
async def summarize(request: SummarizationRequest):
    try:
        summary = summarizer(request.text, max_length=50, min_length=10, do_sample=False)
        return {"summarized_text": summary[0]["summary_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

@app.post("/analyze")
async def analyze_sentiment(request: SentimentAnalysisRequest):
    try:
        result = sentiment_analyzer(request.text)[0]
        return {
            "label": result["label"], 
            "confidence": round(result["score"], 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/submit_quiz")
async def submit_quiz(
    q1: List[str] = Form([]),
    q2: List[str] = Form([]),
    q3: List[str] = Form([]),
    q4: List[str] = Form([]),
    q5: List[str] = Form([]),
):
    """Handles quiz submission and provides feedback."""
    correct_answers = {
        "q1": ["Text generation", "Machine translation", "Conversational AI"],
        "q2": [" Input Embeddings", "Self-Attention Mechanism", "Multi-Head Attention"],
        "q3": ["GPT-3", "BERT", "RoBERTa"],
        "q4": ["Model Size and Parameter Count", "Training Objectives", "Computational Efficiency"],
        "q5": ["Increase in parameter count", "Optimizations for speed and cost-efficiency", "Enhanced attention mechanisms"],
    }
 
    form_data = {"q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5}

    all_correct = True
    results = {}

    for key, correct in correct_answers.items():
        selected = form_data[key] # Access form data directly
        is_correct = len(selected) == len(correct) and all(item in correct for item in selected)
        results[key] = is_correct
        if not is_correct:
            all_correct = False

    if all_correct:
        result_message = "All answers are correct! 🎉"
    else:
        result_message = "Some answers are incorrect. Try again! ❌"

    return {"result": result_message, "results": results}

@app.post("/submit_quiz_2")
async def submit_quiz_2(
    q1: List[str] = Form([]),
    q2: List[str] = Form([]),
    q3: List[str] = Form([]),
    q4: List[str] = Form([]),
    q5: List[str] = Form([]),
):
    """Handles quiz submission and provides feedback."""
    correct_answers = {
        "q1": ["Natural Language Understanding (NLU)", "Content Generation", "Language Translation"],
        "q2": ["Ability to perform zero-shot learning", "Efficient handling of vast amounts of data", "Automation of language-related tasks"],
        "q3": ["High financial costs for training", "Time-intensive training process", " Environmental impact due to high energy consumption"],
        "q4": ["Data collection and preprocessing", "Tokenization and embedding", "Model training and inference"],
        "q5": ["It breaks text into smaller units (tokens) for processing", " It converts words into numerical representations (IDs) for embeddings", "It improves model understanding of text by structuring input data"],
    }
    
    form_data = {"q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5}

    all_correct = True
    results = {}

    for key, correct in correct_answers.items():
        selected = form_data[key] # Access form data directly
        is_correct = len(selected) == len(correct) and all(item in correct for item in selected)
        results[key] = is_correct
        if not is_correct:
            all_correct = False

    if all_correct:
        result_message = "All answers are correct! 🎉"
    else:
        result_message = "Some answers are incorrect. Try again! ❌"

    return {"result": result_message, "results": results}