from fastapi import APIRouter, Form
from typing import List

router = APIRouter()

@router.post("/submit_quiz")
async def submit_quiz(q1: List[str] = Form([]), q2: List[str] = Form([]), q3: List[str] = Form([]), q4: List[str] = Form([]), q5: List[str] = Form([])):
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
        selected = form_data[key]
        is_correct = len(selected) == len(correct) and all(item in correct for item in selected)
        results[key] = is_correct
        if not is_correct:
            all_correct = False
    result_message = "All answers are correct! 🎉" if all_correct else "Some answers are incorrect. Try again! ❌"
    return {"result": result_message, "results": results}

@router.post("/submit_quiz_2")
async def submit_quiz_2(q1: List[str] = Form([]), q2: List[str] = Form([]), q3: List[str] = Form([]), q4: List[str] = Form([]), q5: List[str] = Form([])):
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
        selected = form_data[key]
        is_correct = len(selected) == len(correct) and all(item in correct for item in selected)
        results[key] = is_correct
        if not is_correct:
            all_correct = False
    result_message = "All answers are correct! 🎉" if all_correct else "Some answers are incorrect. Try again! ❌"
    return {"result": result_message, "results": results}
