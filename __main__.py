import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

load_dotenv()

TESTING_GUILD_ID = ID

# the prefix is not used in this example
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")
    print(f"Replied to {interaction.user.name}")

bot.run(os.getenv("TOKEN"))
