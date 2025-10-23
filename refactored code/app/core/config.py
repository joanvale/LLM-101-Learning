import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "LLM101 Learning Lab"
    API_PREFIX = "/llm"
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"
    ALLOWED_HOSTS = ["*"]
    # Extend as needed (DB_URI, secrets, etc.)

settings = Settings()
