from database.supabaseClient import SupaClient
from utils.auth import AuthManager
from utils.weapon import Weapon


class Riven:
    @staticmethod
    def startUnveiling(author, choice):
        registrationID = AuthManager.getRegistrationID(author)
        SupaClient.supabase.table("rivens").insert({
            "riven_type": choice,
            "registration_id": registrationID
        }).execute()

    @staticmethod
    def reveal(author, weapon: str):
        registrationID = AuthManager.getRegistrationID(author)
        weaponID = Weapon.getWeaponID(weapon)
        if weaponID != -1:
            res = SupaClient.supabase.table("rivens").update({"revealed_weapon": weaponID})\
                .eq("registration_id", registrationID).eq("riven_type", Weapon.getTypeID(weapon))\
                .is_("revealed_weapon", "NULL").execute()
            if not res.data:
                return "Weapon type does not match Riven type!"
            return ""
        return "Invalid weapon name"

    @staticmethod
    def getRivenID(author):
        rivens = SupaClient.supabase.table("rivens").select("*, registration(*)") \
            .is_("revealed_weapon", "NULL").execute().data
        result = next((i for i, item in enumerate(rivens) if item["registration"]["guild_id"] == author.guild.id), None)
        return rivens[result]["id"]
