import os

import discord
from dotenv import load_dotenv

from bot import Dealer

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = Dealer(debug_guilds=[1003358734841544734])

client.run(TOKEN)
