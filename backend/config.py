from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "sqlite:///./campaign_tally.db"

    # Supabase Configuration
    SUPABASE_URL: str
    SUPABASE_KEY: str
    SUPABASE_SERVICE_KEY: str
    SUPABASE_DB_PASSWORD: str

    # Full Database URL for SQLAlchemy
    SQLALCHEMY_DATABASE_URL: str

    # Security
    SECRET_KEY: str 
    ALGORITHM: str 
    ACCESS_TOKEN_EXPIRE_MINUTES: int 

    # CORS
    ALLOWED_ORIGINS: List[str]

    class Config:
        env_file = ".env"

settings = Settings()
