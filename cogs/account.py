import discord
from utils.auth import AuthManager


class Account(discord.Cog):
    @discord.slash_command(name="register", description="Register using your discord username")
    async def register(self, ctx):
        AuthManager.registerGuild(ctx.author)
        AuthManager.registerUser(ctx.author)
        await ctx.response.send_message(content=AuthManager.signUp(ctx.author), ephemeral=True)


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Account(bot))  # add the cog to the bot
