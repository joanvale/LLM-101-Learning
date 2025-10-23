from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

router = APIRouter()

# ChatterBot Setup
chatbot = ChatBot("ConversationalBot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

@router.post("/chatbot/")
async def chatbot_endpoint(data: ChatbotRequest):
    user_message = data.message.strip().lower()
    if "hello" in user_message:
        return JSONResponse({"response": "Hello! How can I assist you today?"})
    elif "help" in user_message:
        return JSONResponse({"response": "Sure! What do you need help with?"})
    else:
        response = chatbot.get_response(user_message)
        return JSONResponse({"response": str(response)})
