import os
import discord

from views.dropdown import RivenSelector
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


class GameInit(discord.Cog):
    @discord.slash_command(name="open", description="Open a Riven Mod")
    async def open(self, ctx):
        await ctx.respond("Initiate a betting game!", view=RivenSelector(ctx.author))

    # @discord.slash_command(name="reveal", description="Supabase?")
    # async def open(self, ctx):
    #     res = supabase.table("primary_weapons").select("*").eq('index', 0).execute()
    #     data = res.data
    #     await ctx.respond(data[0]['weapon'] + " " + data[0]['tier'])


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(GameInit(bot))  # add the cog to the bot
