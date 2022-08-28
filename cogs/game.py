import discord
from discord import Option
from database.supaHelper import Helper


class Game(discord.Cog):
    def __init__(self, bot):
        self.rivenPlayer = ""
        self.tableName = ""
        self.ongoing = False
        self.bot = bot

    @discord.slash_command(name="open", description="Open a Riven Mod")
    async def open(self, ctx,
                   riven: Option(str, "Select Riven Mod Type", choices=["Melee", "Rifle", "Pistol"], required=True)):
        choice = -1
        if riven == "Rifle":
            choice = 1
        if riven == "Pistol":
            choice = 2
        if riven == "Melee":
            choice = 3
        Helper.startUnveiling(ctx.author, choice)
        await ctx.response.send_message(f"<@{ctx.author.id}> is currently opening a **{riven} Riven Mod**")

    @discord.slash_command(name="reveal", description="Supabase?")
    async def reveal(self, ctx):
        if self.rivenPlayer == "":
            await ctx.response.send_message("Please use `/open` to open a riven mod", ephemeral=True)
        elif self.rivenPlayer == str(ctx.author):
            self.rivenPlayer = ""
            self.tableName = ""
            self.ongoing = False
            weapon: str = Helper.getMeleeTier("kuva zarr")
            await ctx.respond(weapon)
        else:
            await ctx.response.send_message("Unauthorized", ephemeral=True)


def setup(bot):  # this is called by Pycord to set up the cog
    bot.add_cog(Game(bot))  # add the cog to the bot
