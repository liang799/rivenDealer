import os
import discord

from views.dropdown import RivenSelector
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


class Game(discord.Cog):
    def __init__(self, bot):
        self.rivenPlayer = None
        self.bot = bot

    @discord.slash_command(name="open", description="Open a Riven Mod")
    async def open(self, ctx):
        self.rivenPlayer = ctx.author
        await ctx.response.send_message("Initiate a betting game!", view=RivenSelector(), ephemeral=True)

    @discord.slash_command(name="reveal", description="Supabase?")
    async def reveal(self, ctx):
        if self.rivenPlayer is None:
            await ctx.response.send_message("Please use `/open` to open a riven mod", ephemeral=True)
        elif ctx.author == self.rivenPlayer:
            self.rivenPlayer = None
            res = supabase.table("primary_weapons").select("*").eq('index', 0).execute()
            data = res.data
            await ctx.respond(data[0]['weapon'] + " " + data[0]['tier'])
        else:
            await ctx.response.send_message("Unauthorized", ephemeral=True)


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Game(bot))  # add the cog to the bot
