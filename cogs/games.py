import discord
from discord.ext import commands
import random

## Games Cog ##
# This cog holds all of the minigame commands
class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Basic Rock, Paper, Scissors game
    @commands.command()
    async def rps(self, ctx):
        choices = ["rock", "paper", "scissors"]
        botChoice = random.choice(choices)
        playerChoice = ctx.message.content[5:].lower()
        # Gotta setup these first, otherwise VSC screams
        conditionColour = "#404040"#grey
        outcome = "It's a Tie"
        
        # Tie Condition
        if playerChoice == botChoice:
            outcome == "It's a tie"
            conditionColour = "#404040" #Grey
        # Win conditions
        elif playerChoice == "rock" and botChoice == "scissors" or playerChoice == "paper" and botChoice == "rock" or playerChoice == "scissors" and botChoice == "paper":
            outcome = "You Win!"
            conditionColour = "#00ff00" #Green
        # Else if its not a tie nor a win it must be a loss
        else:
            outcome = "You lost!"
            conditionColour = "#ff0000" #Red
        
        # Create an embed
        embed = discord.Embed(
            colour=discord.Colour.from_str(conditionColour),
            description=f"You chose: {playerChoice.capitalize()} I chose: {botChoice.capitalize()}\n{outcome}"
        )
        embed.set_author(name="Rock Paper Scissors")
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)

async def setup(bot):
    print("Loading games extension...")
    await bot.add_cog(games(bot))