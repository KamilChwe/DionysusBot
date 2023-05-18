import datetime
import random
import discord
from discord.ext import commands
import psutil
import os

## Utility Cog ##
# This cog holds all of the utility commands which help in debuging and stuff along these lines
# This cog is also responsible for all the error handling
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
    ## This basically lets me check if the bot is dead and if not how slow it is
    @commands.command()
    async def ping(self, ctx):
        # Get the bot latency and times it by 1000 to get the ms it took
        await ctx.send(f"Pong!:ping_pong: \nLatency: {round(self.bot.latency * 1000)}ms")

    # Basic help command
    ## DMs the user the commands and how to use them properly
    @commands.command()
    async def help(self, ctx):
                # Core of the embed
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(153,0,204), description="A list of all of the commands Dionysus has to offer.", title="Dionysus' Commands"
        )
        # Additional fields of the embed
        embed.set_author(name="Dionysus' Help")
        embed.add_field(name="Utility", value="Helpful commands for debugging.\n\n**ping: ** Sanity check to see if the bot lives\n**botInfo:** Allows you to see nerdy stats", inline=False)
        embed.add_field(name="Games", value="Minigames!\n\n**RPS: ** Rock, Paper, Scissors. Simply type rps <your choice>", inline=False)
        embed.add_field(name="Character Box", value="Not yet finished", inline=False)
        # Send the completed embed to the user's DM
        # Send a confirmation that the DM has been sent!
        try:
            await ctx.author.send(embed=embed)
            await ctx.message.add_reaction("📨")
            await ctx.send("DM sent!")
        except:
            await ctx.send("Could not send a DM!\nPlease check if you're blocking DMs from unknown users.")
        

    # Bot Statistics
    ## Displays some useful stats about the bots current operations
    @commands.command()
    async def botInfo(self, ctx):
        # Gathering all the necessary info
        uptime = datetime.datetime.now() - self.bot.start_time
        latency = round(self.bot.latency * 1000)
        cpuUsage = psutil.cpu_percent()
        ramUsage = psutil.virtual_memory().percent

        # Core of the embed
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(153,0,204)
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

    # Reloads all of the extensions
    @commands.command()
    async def reload(self, ctx):
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="Reloading."))
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                print(f"Reloading extension {filename[:-3]}")
                await ctx.send(f":arrows_counterclockwise: Reloading extension {filename[:-3]}")
                await self.bot.reload_extension(f"cogs.{filename[:-3]}")
        await ctx.send(":ballot_box_with_check: Reloaded all of the extension!")
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name="type \"=help\""))

# This sets up our cog and adds all of its functionality to the bot client.
async def setup(bot):
    print("Loading utils extension...")
    await bot.add_cog(utils(bot))