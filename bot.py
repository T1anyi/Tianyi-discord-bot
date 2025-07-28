import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')


# discord.Object(id=934629797668200458) My server
GUILD_ID= discord.Object(id=1048428980128198677)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="为了你唱下去"))    
    try:
        print(f'Logged in as {bot.user} (ID: {bot.user.id})')
        bot.tree.clear_commands(guild=None)
        synced = await bot.tree.sync(guild=GUILD_ID)
        print(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(e)
    print("loading ready")


# /echo
@bot.tree.command(name="echo", description="Echoes a message", guild=GUILD_ID)
@app_commands.describe(message="The message to echo")
async def echo(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)

# /hello
@bot.tree.command(name="hello", description="Tianyi says hello", guild=GUILD_ID)
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        '```fix\n大家好,我是虚拟歌手洛天依\n안녕하세요 저는 뤄톈이입니다```',
        file=discord.File("images/tianyi.webp")
    )

# /ping
@bot.tree.command(name="ping", description="Returns pong",guild=GUILD_ID)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong!\n```fix\n{round(bot.latency * 1000)} ms```')

    
bot.run(TOKEN)