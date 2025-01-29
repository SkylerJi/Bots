import discord
from discord.ext import commands
import os
from keep_alive import keep_alive  # This is for keeping the bot online
from dotenv import load_dotenv

load_dotenv()  # Add this before using os.getenv

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(status=discord.Status.online)

# Create a new file called keep_alive.py and put this function in it
keep_alive()  

token = os.getenv('TOKEN')
print(f"Token loaded: {token is not None}")  # Will print True if token exists
bot.run(token)