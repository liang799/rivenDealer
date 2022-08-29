from database.supabaseClient import SupaClient


class Game:
    @staticmethod
    def getOngoingStatus(author):
        response = SupaClient.supabase.table("riven_rollers").select("*").eq('guild_id', author.guild.id).execute()
        if not any(d['revealed'] is None for d in response.data):
            return False
        return True

