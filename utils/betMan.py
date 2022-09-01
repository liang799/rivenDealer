from database.supabaseClient import SupaClient
from utils.auth import AuthManager
from utils.counter import Count
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
            return "Successfully placed bet!"
        else:
            response = SupaClient.supabase.table("speculations").update({
                "id": r.data[0]["id"],
                "registration_id": registrationID,
                "riven_id": rivenID,
                "tier": tierID
            }).execute()
            assert len(response.data) > 0
            return "Updated bet!"

    @staticmethod
    def getNumBets(author):
        rivenID = Riven.getRivenID(author)
        res = SupaClient.supabase.table("speculations").select("id").eq("riven_id", rivenID).execute()
        return Count.countList(res.data)
