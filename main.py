from operator import truediv
import discord
import json

class DionysusClient(discord.Client):
    # When the bot is ready, print a ready ping in console
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

intents = discord.Intents.default()
intents.message_content = True

client = DionysusClient(intents=intents)

# Find a better way to store the token...
with open("token.json") as f:
    token = json.load(f)
    client.run(token['TOKEN'])