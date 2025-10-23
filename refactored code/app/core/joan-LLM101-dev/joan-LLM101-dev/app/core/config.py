from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    DEBUG: bool
    LOG_LEVEL: str
    API_KEY: str
    

    BACKUP_COUNT_FILES: int = 10
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"
    VERSION: str = "1.0.0"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    # Extend as needed (DB_URI, secrets, etc.)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
    
settings = Settings()
