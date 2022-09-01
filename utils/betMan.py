from database.supabaseClient import SupaClient
from utils.auth import AuthManager
from utils.riven import Riven


class BetManager:
    @staticmethod
    def betTier(author, tierID):
        registrationID = AuthManager.getRegistrationID(author)
        rivenID = Riven.getRivenID(author)
        r = SupaClient.supabase.table("speculations").select("id")\
            .eq("registration_id", registrationID).eq("riven_id", rivenID).execute()
        if not r.data:
            response = SupaClient.supabase.table("speculations").insert({
                "registration_id": registrationID,
                "riven_id": rivenID,
                "tier": tierID
            }).execute()
            assert len(response.data) > 0
            return "You have successfully placed your bet!"
        else:
            response = SupaClient.supabase.table("speculations").update({
                "id": r.data[0]["id"],
                "registration_id": registrationID,
                "riven_id": rivenID,
                "tier": tierID
            }).execute()
            assert len(response.data) > 0
            return "You have successfully updated your bet!"
