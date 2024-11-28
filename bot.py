import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os
from keep_alive import keepAlive

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
BASE_URL = os.getenv('BASE_URL')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')


@bot.command()
async def commandname(ctx):
    # Make an API request
    try:
        response = requests.post(BASE_URL)
        if response.status_code == 200:
            await ctx.send(response.text)
        else:
            await ctx.send("Failed to reach API.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

keepAlive()

# Run the bot
bot.run(BOT_TOKEN)
