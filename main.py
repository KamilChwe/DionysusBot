import asyncio
import discord
from discord.ext import commands
import json
import os

# Declaring intents for Discord,
# Not really sure how this works and why but oh well
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
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f"Successfully loaded extension {filename[:-3]}.")
            except:
                print(f"An error occured while loading extension {filename[:-3]}")
    print("Successfully loaded all of the extensions!")

# Main function starts the bot
# Loads the extensions and starts the bot
async def main():
    await load()
    await bot.start(token['TOKEN'])

asyncio.run(main())