import os

from dotenv import load_dotenv
from bot import Dealer

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = Dealer()

client.run(TOKEN)
