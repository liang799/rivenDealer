import discord


class Dealer(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        if message.content.startswith('99!'):
            msg = await message.channel.send('testing123')
