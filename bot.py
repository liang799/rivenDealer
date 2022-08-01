import discord

from views.dropdown import RivenSelector


class MyCog(discord.Cog):
    @discord.slash_command(name="help", description="Display the help panel")
    async def help(self, ctx):
        embed = discord.Embed(title='Help Panel', description='Riven Dealer has a limited vocabulary!')
        embed.add_field(name='/help', value='Display help panel')
        embed.add_field(name='/open', value='Open a Riven Mod')
        embed.add_field(name='/bet', value='Place a bet')
        embed.add_field(name='/forfeit', value='Forfeit placed bet')
        embed.add_field(name='/status', value='Check placed bets')
        embed.add_field(name='/reveal', value='Reveal the Riven Mod')
        await ctx.respond(embed=embed)  # Send the embed with some text

    @discord.slash_command(name="open", description="Open a Riven Mod")
    async def open(self, ctx):
        await ctx.send("Initiate a betting game!", view=RivenSelector(timeout=30))


class Dealer(discord.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_cog(MyCog())

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
