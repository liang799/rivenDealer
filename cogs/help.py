import discord


class HelpPanel(discord.Cog):
    @discord.slash_command(name="help", description="Display the help panel")
    async def help(self, ctx):
        embed = discord.Embed(title='Help Panel', description='Riven Dealer has a limited vocabulary!')
        embed.add_field(name='/help', value='Handy cmds')
        embed.add_field(name='/register', value='Register to start')
        embed.add_field(name='/open', value='Open a Riven Mod')
        embed.add_field(name='/bet', value='Place a bet')
        embed.add_field(name='/forfeit', value='Forfeit placed bet')
        embed.add_field(name='/reveal', value='Reveal the Riven Mod')
        await ctx.respond(embed=embed)  # Send the embed with some text


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(HelpPanel(bot))  # add the cog to the bot
