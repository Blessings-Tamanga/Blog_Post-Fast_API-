from pydantic_settings import BaseSettings
from typing import List

class configSettings(BaseSettings):
    DATABASE_URL: str
    SECRETE_KEY:str
    ALGORITHM: str
    TOKEN_EXPIRE_MINUTES: int
    CORS_ORIGIN: List[str]
    class config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = configSettings()