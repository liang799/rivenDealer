import discord

from views.dropdown import RivenSelector
from database.supaHelper import Helper


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
            weapon: str = Helper.getMeleeTier("kuva zarr")
            await ctx.respond(weapon)
        else:
            await ctx.response.send_message("Unauthorized", ephemeral=True)


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Game(bot))  # add the cog to the bot
