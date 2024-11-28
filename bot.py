import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os
from keep_alive import keepAlive

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
BASE_URL = os.getenv('BASE_URL')
START_ENDPOINT = BASE_URL + "/start"
STOP_ENDPOINT = BASE_URL + "/stop"
STATUS_ENDPOINT = BASE_URL + "/manage-state"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')


@bot.command()
async def mcstart(ctx):
    # Make an API request
    try:
        response = requests.post(START_ENDPOINT)
        if response.status_code == 200:
            await ctx.send(response.text)
        else:
            await ctx.send(
                "Failed to reach the server manager job. If this continues, notify an admin."
            )
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command()
async def mcstop(ctx):
    # Make an API request
    try:
        response = requests.post(STOP_ENDPOINT)
        if response.status_code == 200:
            await ctx.send(response.text)
        else:
            await ctx.send(
                "Failed to reach the server manager job. If this continues, notify an admin."
            )
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command()
async def mcstatus(ctx):
    # Make an API request
    try:
        response = requests.post(STATUS_ENDPOINT)
        if response.status_code == 200:
            await ctx.send(response.text)
        else:
            await ctx.send(
                "Failed to reach the server manager job. If this continues, notify an admin."
            )
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


keepAlive()

# Run the bot
bot.run(BOT_TOKEN)
