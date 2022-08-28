from database.supabaseClient import SupaClient


class AuthManager:
    @staticmethod
    def registerGuild(author):
        guildName = str(author.guild)
        guildID = author.guild.id
        response = SupaClient.supabase.table("guilds").select("*").eq('id', guildID).execute()
        if not response.data:
            data = SupaClient.supabase.table("guilds").insert({
                "id": guildID,
                "guild_name": guildName
            }).execute()
            assert len(data.data) > 0
        else:
            print(f"{guildName} is already inside database")

    @staticmethod
    def signUp(author):
        name = str(author)
        response = SupaClient.supabase.table("users").select("*").eq('id', author.id).execute()
        if not response.data:
            data = SupaClient.supabase.table("users").insert({
                "id": author.id,
                "username": name,
                "guild_id": author.guild.id
            }).execute()
            assert len(data.data) > 0
            return f"Account creation successful! {name} will be stored in the database!"
        else:
            date = response.data[0]['created_at']
            return f"You have already registered. You are a member since {date[0:7]}"

    @staticmethod
    def checkRegistered(author):
        response = SupaClient.supabase.table("users").select("*").eq('id', author.id).execute()
        if not response.data:
            return False
        response = SupaClient.supabase.table("guilds").select("*").eq('id', author.guild.id).execute()
        if not response.data:
            return False
        return True

    @staticmethod
    def auth(author):
        response = SupaClient.supabase.table("riven_rollers").select("*").eq('guild_id', author.guild.id).execute()
        if not any(d['revealed'] is None for d in response.data):
            return False
        return True
