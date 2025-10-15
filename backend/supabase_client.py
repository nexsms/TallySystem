from supabase import create_client, Client
from config import settings
from typing import Optional

_supabase_client: Optional[Client] = None

def get_supabase_client() -> Client:
    """
    Get or create Supabase client instance.
    This is useful for accessing Supabase features like Storage, Realtime, etc.
    """
    global _supabase_client
    
    if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
        raise ValueError(
            "Supabase credentials not configured. "
            "Please set SUPABASE_URL and SUPABASE_KEY in your .env file"
        )
    
    if _supabase_client is None:
        _supabase_client = create_client(
            settings.SUPABASE_URL,
            settings.SUPABASE_KEY
        )
    
    return _supabase_client

def get_supabase_admin_client() -> Client:
    """
    Get Supabase client with service role key for admin operations.
    Use with caution - bypasses Row Level Security (RLS).
    """
    if not settings.SUPABASE_URL or not settings.SUPABASE_SERVICE_KEY:
        raise ValueError(
            "Supabase service key not configured. "
            "Please set SUPABASE_SERVICE_KEY in your .env file"
        )
    
    return create_client(
        settings.SUPABASE_URL,
        settings.SUPABASE_SERVICE_KEY
    )
