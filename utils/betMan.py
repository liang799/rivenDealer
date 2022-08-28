from database.supabaseClient import SupaClient


class BetManager:
    @staticmethod
    def saveCurrentBets(author):
        current = SupaClient.supabase.table("current_bets").select("*").eq('guild_id', author.guild.id).execute()
        assert len(current.data) > 0
        response = SupaClient.supabase.table("bets").insert(current.data).execute()
        assert len(response.data) > 0





