from database.supabaseClient import SupaClient


class Riven:
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
    def startUnveiling(author, choice):
        response = SupaClient.supabase.table("riven_rollers").insert({
            "riven_type": choice,
            "user_id": author.id,
            "guild_id": author.guild.id
        }).execute()

    # @staticmethod
    # def reveal(author, weapon: str):
