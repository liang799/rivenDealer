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
        if not self.ongoing:
            self.ongoing = True
            self.rivenPlayer = str(ctx.author)
            if riven == "Melee":
                self.tableName = "melee_weapons"
            if riven == "Rifle":
                self.tableName = "primary_weapons"
            if riven == "Pistol":
                self.tableName = "secondary_weapons"
            await ctx.response.send_message(f"<@{ctx.author.id}> is currently opening a **{riven} Riven Mod**")
        else:
            await ctx.response.send_message("Please wait for the current round to end", ephemeral=True)

    @discord.slash_command(name="eveal", description="Supabase?")
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
