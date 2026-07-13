from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/aivoa")
    api_port: int = 8000
    api_host: str = "0.0.0.0"
    debug: bool = True
    environment: str = "development"
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:5173", "http://localhost:8000"]
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")
    llm_model: str = "gemma2-9b-it"
    llm_temperature: float = 0.7
    llm_max_tokens: int = 1000
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
