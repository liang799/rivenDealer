from database.supabaseClient import SupaClient
from utils.auth import AuthManager


class Game:
    @staticmethod
    def getOngoingStatus(author):
        # response = SupaClient.supabase.table("rivens").select("*, registration(guild_id)")\
        #     .eq("registration.guild_id", author.guild.id).is_("revealed_weapon", "NULL").execute()
        rivens = SupaClient.supabase.table("rivens").select("*, registration(*)")\
            .is_("revealed_weapon", "NULL").execute().data
        result = list(filter(lambda riven: riven["registration"]["guild_id"] == author.guild.id, rivens))
        if len(result) != 0:
            return True
        return False

    @staticmethod
    def getResults(author):
        registrationID = AuthManager.getRegistrationID(author)
        res = SupaClient.supabase.table("rivens").select("id")\
            .eq("registration_id", registrationID).is_("revealed_weapon", "NULL").execute()
        print(res.data)
        rivenID = res.data[0]["id"]
        res = SupaClient.supabase.table("speculations").select(
            "registration: registration_id(user_id),"
            "weapon_tiers: tier(name)"
        ).eq("riven_id", rivenID).execute()
        print(res.data)
        return res.data
