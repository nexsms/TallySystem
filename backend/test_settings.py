from config import settings

def test_settings():
    print("✅ SUPABASE_URL:", settings.SUPABASE_URL)
    print("✅ DATABASE_URL:", settings.DATABASE_URL)
    print("✅ SQLALCHEMY_DATABASE_URL:", settings.SQLALCHEMY_DATABASE_URL)
    print("✅ ALLOWED_ORIGINS:", settings.ALLOWED_ORIGINS)
    print("✅ SECRET_KEY:", settings.SECRET_KEY[:8] + "..." if settings.SECRET_KEY else "❌ missing")

if __name__ == "__main__":
    test_settings()
