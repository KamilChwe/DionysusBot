import discord
from discord.ext import commands
import graphene
import requests
import aiohttp

class anilist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def Anime(self, ctx, search: str):
        url = "https://graphql.anilist.co"

        query = """
        query($search: String) {
            Media (search: $search, type: ANIME) {
                title {
                    english
                    romaji
                    native
                }
                id
                bannerImage
                favourites
                description(asHtml:false)
                episodes
                nextAiringEpisode {
                    episode
                }
                meanScore
                startDate{
                    year
                    month
                    day
                }
            }
        }
        """

        # Set "seach" as the content of the message (excluding command)
        variables = {
            'search': ctx.message.content[8]
        }

        # Crete an async request for the data required
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, json={"query": query, "variables": variables}
            ) as r:
                # If the status recieved is 200 that measn everything is all good and we got data
                if r.status == 200:
                    info = await r.json()
                    media = info["data"]["Media"]
                    text = media["description"]
                    desc = text[:text.find("<br></br>") + 1][:-1]
                    embed = discord.Embed(
                    title = (media["title"]["english"]),
                    description = (str(desc)),
                    colour = discord.Colour.purple()
                    )
                    # Create and embed for the data
                    embed.set_footer(text=(str(media["id"])))
                    embed.set_image(url=(media["bannerImage"]))
                    embed.set_author(name="Anime Information.",
                    icon_url="https://33.media.tumblr.com/1a6093f3b0605406cdc2bffa524a39ad/tumblr_n7ymbgucKv1r4kyupo1_500.gif")
                    embed.add_field(name="Native:", value=(media["title"]["native"]), inline =True)
                    embed.add_field(name="Romaji:", value=(media["title"]["romaji"]), inline =True)
                    #embed.add_field(name="Start Date:", value=(str(media["startDate"]["day"]["month"]["year"])), inline =True)
                    embed.add_field(name="Mean Score:", value=("{}%".format(str(media["meanScore"]))), inline =True)
                    embed.add_field(name="Episodes:", value=(str(media["nextAiringEpisode"]["episode"]-1) +"/"+str(media["episodes"])), inline =True)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Couldn't find Anime with provided code...", delete_after=15)
                    

async def setup(bot):
    print("Loading AniList extension...")
    await bot.add_cog(anilist(bot))