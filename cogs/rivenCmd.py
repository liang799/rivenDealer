import os
import discord

from views.dropdown import RivenSelector
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


class Commands(discord.Cog):
    @discord.slash_command(name="open", description="Open a Riven Mod")
    async def open(self, ctx):
        await ctx.send("Initiate a betting game!", view=RivenSelector(timeout=30))

    @discord.slash_command(name="reveal", description="Supabase?")
    async def open(self, ctx):
        res = supabase.table("primary_weapons").select("*").eq('index', 0).execute()
        data = res.data
        await ctx.send(data[0]['weapon'] + " " + data[0]['tier'])


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Commands(bot))  # add the cog to the bot
