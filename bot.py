import discord
import asyncio
from discord.ext import commands
import os

prefix = "+"
bot = commands.Bot(command_prefix=prefix)

TOKEN = "OTY3NDY2ODU5NTM4NTQ2Njg5.YmQtuQ.RLFjvfpOtKbchrWElWoFBTrMEE0"


@bot.event
async def on_ready():
    print("Subscribe the channel :)")


# @bot.command()
# async def ping(ctx):
#     await ctx.send("PONG!")


for cog in os.listdir(r"C:\Users\sadhikari\Desktop\Covid Discord bot\cogs"):
    if cog.endswith(".py"):
        try:
            cog=f"cogs.{cog.replace('.py','')}"
            bot.load_extension(cog)
            
        except Exception as e:
            print(f"{cog} cannot be loaded")
            raise e



bot.run(TOKEN)