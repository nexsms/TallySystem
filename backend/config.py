from pydantic_settings import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: Optional[str] = None

    # Supabase Configuration
    SUPABASE_URL: str = "https://lvugkevhqnhtilzqbyei.supabase.co"
    SUPABASE_KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx2dWdrZXZocW5odGlsenFieWVpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjAzMzY1OTksImV4cCI6MjA3NTkxMjU5OX0.oxdRBvtk-zgxQGnsD814-DQsxaPcwt_pK6VulsD-EVI"
    SUPABASE_SERVICE_KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx2dWdrZXZocW5odGlsenFieWVpIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MDMzNjU5OSwiZXhwIjoyMDc1OTEyNTk5fQ.NHr12oXpyEXC-zAsGJo-COlbD6XzlsIdHgHMTbYDNjw"
    SUPABASE_DB_PASSWORD: str = "pHagBTJIKLlyJCFw"

    # Full Database URL for SQLAlchemy
    SQLALCHEMY_DATABASE_URL: str = f"postgresql://postgres:pHagBTJIKLlyJCFw@db.lvugkevhqnhtilzqbyei.supabase.co:5432/postgres"

    # Security
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "*"]

    class Config:
        env_file = ".env"

settings = Settings()
