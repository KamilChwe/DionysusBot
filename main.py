import asyncio
import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="=", intents=intents, help_command=None)

# Load the token from the JSON file
with open("token.json") as f:
    token = json.load(f)

# Goes through each file in the cogs folder and loads it
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(token['TOKEN'])

asyncio.run(main())