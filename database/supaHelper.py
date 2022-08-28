import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()


class Helper:
    __url: str = os.getenv("SUPABASE_URL")
    __key: str = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(__url, __key)

    @staticmethod
    def getMeleeTier(weapon: str):
        weaponCaps = weapon.upper()
        res = Helper.supabase.table("primary_weapons").select("*").eq('weapon', weaponCaps).execute()
        data = res.data
        tier: str = data[0]['tier']
        return tier

    @staticmethod
    def signUp(name: str):
        response = Helper.supabase.table("users").select("username").eq('username', name).execute()
        result = response.data
        if not any(d['username'] == name for d in result):
            data = Helper.supabase.table("users").insert({"username": name}).execute()
            assert len(data.data) > 0



