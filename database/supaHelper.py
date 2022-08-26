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
        userName = Helper.supabase.table("user_bets").select("user").eq('user', name).execute()
        print(userName)
        if userName is not name:
            data = Helper.supabase.table("user_bets").insert({"user": name}).execute()
            assert len(data.data) > 0



