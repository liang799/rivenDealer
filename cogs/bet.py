import discord
from discord import Option

from utils.auth import AuthManager
from utils.betMan import BetManager
from utils.game import Game


class Bet(discord.Cog):
    @discord.slash_command(name="bet", description="Speculate Unveiled Riven Tier")
    async def bet(self, ctx, tier: Option(str, "Select Riven Mod Type", choices=["S", "A", "B", "C", "D", "Unknown"],
                                          required=True)):
        if AuthManager.checkRegistered(ctx.author):
            if Game.getOngoingStatus(ctx.author):
                choice = -1
                if tier == "S":
                    choice = 1
                if tier == "A":
                    choice = 2
                if tier == "B":
                    choice = 3
                if tier == "C":
                    choice = 4
                if tier == "D":
                    choice = 5
                if tier == "Unknown":
                    choice = 6
                message = BetManager.betTier(ctx.author, choice)
                await ctx.response.send_message(message, ephemeral=True)
            else:
                await ctx.response.send_message("Please initialise the game with `/open`", ephemeral=True)
        else:
            await ctx.response.send_message("Please use `/register` to register", ephemeral=True)

    @discord.slash_command(name="status", description="Check number of bets")
    async def status(self, ctx):
        if AuthManager.checkRegistered(ctx.author):
            if Game.getOngoingStatus(ctx.author):
                num = BetManager.getNumBets(ctx.author)
                embed = discord.Embed(title="Current round", description=f"Number of bets: {num}")
                await ctx.respond(embed=embed, ephemeral=True)  # Send the embed with some text
            else:
                await ctx.response.send_message("Please initialise the game with `/open`", ephemeral=True)
        else:
            await ctx.response.send_message("Please use `/register` to register", ephemeral=True)


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Bet(bot))  # add the cog to the bot
