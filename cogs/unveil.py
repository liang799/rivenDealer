import discord
from discord import Option

from utils.auth import AuthManager
from utils.game import Game
from utils.riven import Riven


class Roller(discord.Cog):
    @discord.slash_command(name="open", description="Open a Riven Mod")
    async def open(self, ctx,
                   riven: Option(str, "Select Riven Mod Type", choices=["Melee", "Rifle", "Pistol"], required=True)):
        if not Game.getOngoingStatus(ctx.author):
            choice = -1
            if riven == "Rifle":
                choice = 1
            if riven == "Pistol":
                choice = 2
            if riven == "Melee":
                choice = 3
            if AuthManager.checkRegistered(ctx.author):
                Riven.startUnveiling(ctx.author, choice)
                await ctx.response.send_message(f"<@{ctx.author.id}> is currently opening a **{riven} Riven Mod**")
            else:
                await ctx.response.send_message("Please use `/register` to register", ephemeral=True)
        else:
            await ctx.response.send_message("Please wait for the current round to end", ephemeral=True)

    @discord.slash_command(name="reveal", description="Supabase?")
    async def reveal(self, ctx):
        if AuthManager.checkRegistered(ctx.author):
            if Game.getOngoingStatus(ctx.author):
                test = Riven.getType("kuva zarr")
                await ctx.respond(test)
            else:
                await ctx.response.send_message("Please use `/open` to open a riven mod", ephemeral=True)
        else:
            await ctx.response.send_message("Please use `/register` to register", ephemeral=True)


def setup(bot):  # this is called by Pycord to set up the cog
    bot.add_cog(Roller(bot))  # add the cog to the bot
