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
            SupaClient.supabase.table("rivens").update({"revealed_weapon": weaponID})\
                .eq('registration_id', registrationID).eq('riven_type', Weapon.getTypeID(weapon))\
                .is_('revealed_weapon', None).execute()
            return "Success!"
        return "Invalid weapon name"
