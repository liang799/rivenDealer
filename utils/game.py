from database.supabaseClient import SupaClient


class Game:
    @staticmethod
    def getOngoingStatus(author):
        response = SupaClient.supabase.table("riven_rollers").select("*").eq('guild_id', author.guild.id).execute()
        if not any(d['revealed'] is None for d in response.data):
            return False
        return True

    @staticmethod
    def startUnveiling(author, choice):
        response = SupaClient.supabase.table("riven_rollers").insert({
            "riven_type": choice,
            "user_id": author.id,
            "guild_id": author.guild.id
        }).execute()
