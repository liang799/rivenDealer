from database.supabaseClient import SupaClient


class Game:
    @staticmethod
    def getOngoingStatus(author):
        # response = SupaClient.supabase.table("rivens").select('*, registration(guild_id)')\
        #     .eq('registration.guild_id', author.guild.id).is_("revealed_weapon", "NULL").execute()
        rivens = SupaClient.supabase.table("rivens").select('*, registration(*)')\
            .is_("revealed_weapon", "NULL").execute().data
        result = list(filter(lambda riven: riven['registration']['guild_id'] == author.guild.id, rivens))
        if len(result) != 0:
            return True
        return False
