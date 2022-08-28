import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()


class Helper:
    __url: str = os.getenv("SUPABASE_URL")
    __key: str = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(__url, __key)

    @staticmethod
    def getTier(weapon: str):
        weaponCaps = weapon.upper()
        res = Helper.supabase.table("weapons").select("*").eq('weapon', weaponCaps).execute()
        data = res.data
        tier: str = data[0]['tier']
        return tier

    @staticmethod
    def registerGuild(author):
        guildName = str(author.guild)
        guildID = author.guild.id
        response = Helper.supabase.table("guilds").select("*").eq('id', guildID).execute()
        if not response.data:
            data = Helper.supabase.table("guilds").insert({
                "id": guildID,
                "guild_name": guildName
            }).execute()
            assert len(data.data) > 0
        else:
            print(f"{guildName} is already inside database")

    @staticmethod
    def signUp(author):
        name = str(author)
        response = Helper.supabase.table("users").select("*").eq('id', author.id).execute()
        if not response.data:
            data = Helper.supabase.table("users").insert({
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
        response = Helper.supabase.table("users").select("*").eq('id', author.id).execute()
        if not response.data:
            return False
        response = Helper.supabase.table("guilds").select("*").eq('id', author.guild.id).execute()
        if not response.data:
            return False
        return True

    @staticmethod
    def startUnveiling(author, choice):
        response = Helper.supabase.table("riven_rollers").insert({
            "riven_type": choice,
            "user_id": author.id,
            "guild_id": author.guild.id
        }).execute()

    @staticmethod
    def getOngoingStatus(author):
        response = Helper.supabase.table("riven_rollers").select("*").eq('guild_id', author.guild.id).execute()
        if not any(d['revealed'] is None for d in response.data):
            return False
        return True

    @staticmethod
    def saveCurrentBets(author):
        current = Helper.supabase.table("current_bets").select("*").eq('guild_id', author.guild.id).execute()
        assert len(current.data) > 0
        response = Helper.supabase.table("bets").insert(current.data).execute()
        assert len(response.data) > 0





