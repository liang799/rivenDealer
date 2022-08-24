import discord

cogs_list = [
    'helpPanel',
    'gameInit'
]


class Dealer(discord.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for cog in cogs_list:
            self.load_extension(f'cogs.{cog}')

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
