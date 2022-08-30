from database.supabaseClient import SupaClient


class Weapon:
    @staticmethod
    def getWeaponID(weapon: str):
        weaponCaps = weapon.upper()
        res = SupaClient.supabase.table("weapons").select(
            "index"
        ).eq('weapon', weaponCaps).execute()
        if not res.data:
            return -1
        return res.data[0]["index"]

    @staticmethod
    def getTierID(weapon: str):
        weaponCaps = weapon.upper()
        res = SupaClient.supabase.table("weapons").select(  # Kind of like joining tables
            "weapon_tiers(index)"
        ).eq('weapon', weaponCaps).execute()
        if not res.data:
            return -1
        return res.data[0]['weapon_tiers']['index']

    @staticmethod
    def getTypeID(weapon: str):
        weaponCaps = weapon.upper()
        res = SupaClient.supabase.table("weapons").select(  # Kind of like joining tables
            "weapon_types(index)"
        ).eq('weapon', weaponCaps).execute()
        if not res.data:
            return -1
        return res.data[0]['weapon_types']['index']

    @staticmethod
    def getTier(weapon: str):
        weaponCaps = weapon.upper()
        res = SupaClient.supabase.table("weapons").select(  # Kind of like joining tables
            "weapon_tiers(name)"
        ).eq('weapon', weaponCaps).execute()
        if not res.data:
            return "Invalid weapon name"
        return res.data[0]['weapon_tiers']['name']

    @staticmethod
    def getType(weapon: str):
        weaponCaps = weapon.upper()
        res = SupaClient.supabase.table("weapons").select(  # Kind of like joining tables
            "weapon_types(type)"
        ).eq('weapon', weaponCaps).execute()
        if not res.data:
            return "Invalid weapon name"
        return res.data[0]['weapon_types']['type']

    @staticmethod
    def getWeaponsCol():
        res = SupaClient.supabase.table("weapons").select("weapon").execute()
        return res
