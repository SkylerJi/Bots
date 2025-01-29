import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # This is helpful for local development

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(status=discord.Status.online)

token = os.getenv('TOKEN')
print(f"Token loaded: {token is not None}")  # Will print True if token exists
bot.run(token)