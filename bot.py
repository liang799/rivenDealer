import discord


class MyCog(discord.Cog):
    @discord.slash_command(name="test")
    async def test(self, ctx):
        await ctx.respond("TEST")


class Dealer(discord.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_cog(MyCog())

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
