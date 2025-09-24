from functools import lru_cache

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
        Application configuration.
    """
    DATABASE_URL: str
    
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_TOKEN_EXPIRY: int
    
    IP_HOST: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()