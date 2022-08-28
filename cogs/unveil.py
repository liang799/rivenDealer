import discord
from discord import Option
from database.supaHelper import Helper


class Roller(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="open", description="Open a Riven Mod")
    async def open(self, ctx,
                   riven: Option(str, "Select Riven Mod Type", choices=["Melee", "Rifle", "Pistol"], required=True)):
        if not Helper.getOngoingStatus(ctx.author):
            choice = -1
            if riven == "Rifle":
                choice = 1
            if riven == "Pistol":
                choice = 2
            if riven == "Melee":
                choice = 3
            if Helper.checkRegistered(ctx.author):
                Helper.startUnveiling(ctx.author, choice)
                await ctx.response.send_message(f"<@{ctx.author.id}> is currently opening a **{riven} Riven Mod**")
            else:
                await ctx.response.send_message("Please use `/register` to register", ephemeral=True)
        else:
            await ctx.response.send_message("Please wait for the current round to end", ephemeral=True)

    @discord.slash_command(name="reveal", description="Supabase?")
    async def reveal(self, ctx):
        if Helper.checkRegistered(ctx.author):
            if Helper.getOngoingStatus(ctx.author):
                weapon: str = Helper.getTier("kuva zarr")
                await ctx.respond(weapon)
            else:
                await ctx.response.send_message("Please use `/open` to open a riven mod", ephemeral=True)
        else:
            await ctx.response.send_message("Please use `/register` to register", ephemeral=True)


def setup(bot):  # this is called by Pycord to set up the cog
    bot.add_cog(Roller(bot))  # add the cog to the bot
