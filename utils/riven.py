from database.supabaseClient import SupaClient


class Riven:
    @staticmethod
    def getTier(weapon: str):
        weaponCaps = weapon.upper()
        res = SupaClient.supabase.table("weapons").select("*").eq('weapon', weaponCaps).execute()
        data = res.data
        tier: str = data[0]['tier']
        return tier
