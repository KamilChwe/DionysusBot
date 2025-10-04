import discord
from discord.ext import commands
import requests

## Anilist Cog ##
# This cog is responsible for gathering information from Anilist and displaying it on Discord
class Anilist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    url = "https://graphql.anilist.co"

    @commands.command()
    async def anime(self,ctx):
        await ctx.send(f"ctx = {ctx.message}")

async def setup(bot):
    print("Loading anilist extension...")
    await bot.add_cog(Anilist(bot))