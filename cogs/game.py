import discord
from discord import Option
from database.supaHelper import Helper


class Game(discord.Cog):
    def __init__(self, bot):
        self.rivenPlayer = ""
        self.tableName = ""
        self.bot = bot

    @discord.slash_command(name="open", description="Open a Riven Mod")
    async def open(self, ctx,
                   riven: Option(str, "Select Riven Mod Type", choices=["Melee", "Rifle", "Pistol"], required=True)):
        self.rivenPlayer = str(ctx.author)
        Helper.signUp(self.rivenPlayer)  # try to sign up
        if riven == "Melee":
            self.tableName = "melee_weapons"
        if riven == "Rifle":
            self.tableName = "primary_weapons"
        if riven == "Pistol":
            self.tableName = "secondary_weapons"
        await ctx.response.send_message(f"<@{ctx.author.id}> is currently opening a **{riven} Riven Mod**")

    @discord.slash_command(name="reveal", description="Supabase?")
    async def reveal(self, ctx):
        if self.rivenPlayer == "":
            await ctx.response.send_message("Please use `/open` to open a riven mod", ephemeral=True)
        elif str(ctx.author) == self.rivenPlayer:
            self.rivenPlayer = ""
            weapon: str = Helper.getMeleeTier("kuva zarr")
            await ctx.respond(weapon)
        else:
            await ctx.response.send_message("Unauthorized", ephemeral=True)

    @discord.slash_command(name="test", description="Supabase?")
    async def test(self, ctx):
        Helper.signUp(self.rivenPlayer)
        await ctx.response.send_message(self.rivenPlayer)

    @discord.slash_command(name="options", description="slash?")
    async def options(self, ctx, test: Option(str, "reaction you want", choices=["Hi", "image"], required=True)):
        if test == "Hi":
            await ctx.response.send_message("sjdfld")
        if test == "image":
            await ctx.response.send_message("ajksdjjkkkkkkkk")


def setup(bot):  # this is called by Pycord to set up the cog
    bot.add_cog(Game(bot))  # add the cog to the bot
