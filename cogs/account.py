import discord
from database.supaHelper import Helper


class Account(discord.Cog):
    @discord.slash_command(name="register", description="Register using your discord username")
    async def register(self, ctx):
        await ctx.response.send_message(content=Helper.signUp(str(ctx.author)), ephemeral=True)


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(Account(bot))  # add the cog to the bot
