import os

from dotenv import load_dotenv

from bot import Dealer

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = Dealer(debug_guilds=[1012051832987734127, 1013390714916319283])

client.run(TOKEN)
