import discord
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot(debug_guilds=[655039890991611904])

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.send("Hey!")

@bot.event
async def on_member_join(member : discord.Member):
    print(f'{member.name.title()}')


bot.run(os.getenv('DISCORD_TOKEN')) # run the bot with the token