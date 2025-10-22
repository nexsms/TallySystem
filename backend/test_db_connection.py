
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
import os

print(f"SQLALCHEMY_DATABASE_URL: {settings.SQLALCHEMY_DATABASE_URL}")

try:
    engine = create_engine(
        settings.SQLALCHEMY_DATABASE_URL,
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db = SessionLocal()
    db.execute("SELECT 1")
    print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")
