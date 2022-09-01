from database.supabaseClient import SupaClient
from utils.auth import AuthManager
from utils.riven import Riven


class BetManager:
    @staticmethod
    def betTier(author, tierID):
        registrationID = AuthManager.getRegistrationID(author)
        rivenID = Riven.getRivenID(author)
        response = SupaClient.supabase.table("speculations").insert({
            "registration_id": registrationID,
            "riven_id": rivenID,
            "tier": tierID
        }).execute()
        assert len(response.data) > 0
