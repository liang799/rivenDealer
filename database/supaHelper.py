import os
import time
from datetime import datetime

from dotenv import load_dotenv
from supabase import create_client, Client
from dateutil import parser

load_dotenv()


class Helper:
    __url: str = os.getenv("SUPABASE_URL")
    __key: str = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(__url, __key)

    @staticmethod
    def getMeleeTier(weapon: str):
        weaponCaps = weapon.upper()
        res = Helper.supabase.table("primary_weapons").select("*").eq('weapon', weaponCaps).execute()
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
            print("Already inside")

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
            print(date)
            # date_time = parser.parse(date)
            # unixtime = time.mktime(date_time.timetuple())
            # return f"You have already registered. You are a member since <t:{unixtime}:R>"

            dObj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f%z")
            unixtime = time.mktime(dObj.timetuple())
            return f"You have already registered. You are a member since <t:{unixtime}>"

            # return f"You have already registered. You are a member since {date[0:7]}"

    @staticmethod
    def getOngoingStatus(author):
        response = Helper.supabase.table("riven_rollers").select("*").eq('roller_id', author.id).execute()





