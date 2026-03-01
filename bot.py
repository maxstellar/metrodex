import discord
from discord import ui
from discord.ext import tasks, commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
server = discord.Object(id=1081625448385085440)

bot = commands.Bot(command_prefix="m!", intents=intents)

@tasks.loop(minutes=1)
async def send_interval_message():
    channel = bot.get_channel(1477473312291553453)
    await channel.send("A wild metro station appeared. Metro station tentative")
    print("Spawned!")

@bot.event
async def on_ready():
    bot.tree.copy_global_to(guild=server)
    await bot.tree.sync(guild=server)
    print(f"Logged in as {bot.user}")
    send_interval_message.start()
    print("Started spawns!")

@bot.tree.command(name="ping", description="Returns the latency of the bot.")
async def ping(interaction: discord.Interaction):
    latency_ms = round(bot.latency * 1000, 2)
    await interaction.response.send_message(f'Pong! **{latency_ms}ms**')

bot.run(TOKEN)