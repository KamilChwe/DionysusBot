import discord
from discord.ext import commands
import random

## Character Cog ##
# The old "charabox" makes a comeback :sunglasses:
class chara(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def charabox(self, ctx):
        quality = random.randint(1, 100)
        # L - 1%
        # E - 10%
        # U - 30%
        # C - 59%
        if(quality == 1):
            await ctx.send("Quality: Legendary")
        elif(quality >= 2 and quality <= 12):
            await ctx.send("Quality: Epic")
        elif(quality >= 13 and quality <= 33):
            await ctx.send("Quality: Uncommon")
        else:
            await ctx.send("Quality: Common")


async def setup(bot):
    print("Loading Character extension...")
    await bot.add_cog(chara(bot))