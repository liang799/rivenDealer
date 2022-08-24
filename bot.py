import discord
import os

from views.dropdown import RivenSelector
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


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

    @discord.slash_command(name="reveal", description="Supabase?")
    async def open(self, ctx):
        res = supabase.table("primary_weapons").select("*").eq('index', 0).execute()
        data = res.data
        print(data)
        await ctx.send(data[0]['weapon'] + " " + data[0]['tier'])


class Dealer(discord.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_cog(MyCog())

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
