import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()


class SupaClient:
    __url: str = os.getenv("SUPABASE_URL")
    __key: str = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(__url, __key)
