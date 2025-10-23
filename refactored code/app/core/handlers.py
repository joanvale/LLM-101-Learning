from transformers import pipeline
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from deep_translator import GoogleTranslator

# Initialize once
generator = pipeline("text-generation", model="gpt2")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment_analyzer = pipeline("sentiment-analysis")

chatbot = ChatBot("ConversationalBot")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def generate_text(prompt: str):
    return generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]

def summarize_text(text: str):
    return summarizer(text, max_length=50, min_length=10, do_sample=False)[0]["summary_text"]

def analyze_sentiment(text: str):
    result = sentiment_analyzer(text)[0]
    return {"label": result["label"], "confidence": round(result["score"], 2)}

def translate_text(text: str, target_language: str):
    translator = GoogleTranslator(source="auto", target=target_language)
    return translator.translate(text)

def chatbot_response(message: str):
    message = message.strip().lower()
    if "hello" in message:
        return "Hello! How can I assist you today?"
    elif "help" in message:
        return "Sure! What do you need help with?"
    return str(chatbot.get_response(message))
