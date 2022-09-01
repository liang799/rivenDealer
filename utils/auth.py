from database.supabaseClient import SupaClient


class AuthManager:
    @staticmethod
    def registerGuild(author):
        guildName = str(author.guild)
        res = SupaClient.supabase.table("discord_guilds").upsert({
            "id": author.guild.id,
            "guild_name": guildName
        }).execute()
        assert len(res.data) > 0

    @staticmethod
    def registerUser(author):
        userName = str(author)
        res = SupaClient.supabase.table("discord_users").upsert({
            "id": author.id,
            "username": userName
        }).execute()
        assert len(res.data) > 0

    @staticmethod
    def signUp(author):
        response = SupaClient.supabase.table("registration").select("*")\
            .eq("user_id", author.id).eq("guild_id", author.guild.id).execute()
        if not response.data:
            res = SupaClient.supabase.table("registration").insert({
                "user_id": author.id,
                "guild_id": author.guild.id
            }).execute()
            assert len(res.data) > 0
            return f"Account creation successful!"
        else:
            date = response.data[0]["created_at"]
            return f"You have already registered. You are a member since {date[0:7]}"

    @staticmethod
    def checkRegistered(author):
        response = SupaClient.supabase.table("registration").select("*") \
            .eq("user_id", author.id).eq("guild_id", author.guild.id).execute()
        if not response.data:
            return False
        return True

    @staticmethod
    def getRegistrationID(author):
        response = SupaClient.supabase.table("registration").select("id") \
            .eq("user_id", author.id).eq("guild_id", author.guild.id).execute()
        if not response.data:
            return -1
        return response.data[0]["id"]


