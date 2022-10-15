import datetime
import random
import discord
from discord.ext import commands
import psutil

## Utility Cog ##
# This cog holds all of the utility commands which help in debuging and stuff along these lines
class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # When the bot is ready sent a message to the console
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.start_time = datetime.datetime.now()
        print(f"Start Time: {self.bot.start_time}")
        print("Dionysus: Online")

    # Basic ping command
    @commands.command()
    async def ping(self, ctx):
        # Get the bot latency and times it by 1000 to get the ms it took
        await ctx.send(f"Pong! \n Latency: {round(self.bot.latency * 1000)}ms")
    
    # Bot Statistics
    @commands.command()
    async def botInfo(self, ctx):
        uptime = datetime.datetime.now() - self.bot.start_time
        latency = round(self.bot.latency * 1000)
        cpuUsage = psutil.cpu_percent()
        ramUsage = psutil.virtual_memory().percent

        # Core of the embed
        embed = discord.Embed(
            color=discord.Colour.from_rgb(153,0,204)
        )
        # Additional fields of the embed
        embed.set_footer(text=f"Requested by: {ctx.author}")
        embed.set_author(name="Bot's Statistics")
        embed.add_field(name="Uptime", value=str(uptime)[:-4])
        embed.add_field(name="Latency", value=str(latency) + 'ms')
        embed.add_field(name="Wine Level", value=f"{random.randint(10,100)}%")
        embed.add_field(name="CPU usage", value=f"{str(cpuUsage)}%")
        embed.add_field(name="RAM Usage", value=f"{str(ramUsage)}%")
        # Send the completed embed
        await ctx.send(embed=embed)

# This sets up our cog and adds all of its functionality to the bot client.
async def setup(bot):
    await bot.add_cog(utils(bot))
