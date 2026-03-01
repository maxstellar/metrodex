import time
import random
import discord
from discord import ui, app_commands
from discord.ext import tasks, commands
from dotenv import load_dotenv
import os

station_data = {
    "191st Street": [
        "At roughly 180 feet below street level, this is the deepest station in the NYC subway system.",
        "It can be accessed via a long underground pedestrian tunnel stretching nearly a full city block from the street entrance to the platform."
    ],
    "Borough Hall": [
        "This station opened in 1908 and features some of the most well-preserved Heins & LaFarge tilework in the system.",
        "It sits beneath Brooklyn's civic center, directly below the building that serves as the borough's seat of government."
    ],
    "Jay Street–MetroTech": [
        "The MTA's own headquarters is located directly above this station, making it the administrative heart of the subway system.",
        "Its F and R platforms occupy different levels, making it one of the more architecturally layered stations in Brooklyn."
    ],
    "Court Square": [
        "This station is one of the few places where riders can transfer between the G and the 7 train, making it a crucial Queens connector.",
        "It sits in the heart of Long Island City, one of the fastest-developing neighborhoods in the city."
    ],
    "Jackson Heights–Roosevelt Avenue": [
        "This station serves one of the most ethnically diverse neighborhoods on earth — the surrounding zip code has been called the most diverse in the United States.",
        "The elevated 7 train platform runs directly above a busy commercial corridor, giving riders a sweeping view of the street life below."
    ],
    "South Ferry": [
        "This is the southernmost station in Manhattan and the southern terminus of its line.",
        "It was severely damaged by Hurricane Sandy in 2012 and required years of reconstruction before reopening."
    ],
    "Coney Island–Stillwell Avenue": [
        "This is the largest elevated terminal in the entire NYC subway system, with four lines terminating here under one roof.",
        "It sits at the edge of a famous beachside neighborhood in southern Brooklyn, steps from the boardwalk."
    ],
    "161st Street–Yankee Stadium": [
        "This station is named after one of the most famous sports venues in American history, located directly across the street.",
        "The elevated B/D platform offers a direct sightline to the stadium, making it one of the most visually iconic station approaches in the Bronx."
    ],
    "34th Street–Herald Square": [
        "This station sits directly beneath the flagship location of one of the most famous department stores in the world.",
        "It is one of the busiest stations in the system during the holiday season, when the neighborhood above draws enormous shopping crowds."
    ],
    "14th Street–Union Square": [
        "This station connects the East Side express and local lines to the crosstown L, making it one of the most important transfer points in lower Manhattan.",
        "The plaza above it hosts a famous outdoor greenmarket several days a week, one of the largest open-air farmers markets in the country."
    ],
    "Fulton Street": [
        "This Lower Manhattan hub was extensively rebuilt following the September 11 attacks into a modern transit center.",
        "Its Dey Street Passageway connects it to the Cortlandt Street station, forming one of the longest underground pedestrian corridors in the city."
    ],
    "72nd Street": [
        "This station is part of the original 1904 IRT line, and its classical terra cotta plaques and detailing are largely intact over a century later.",
        "It sits at the heart of the Upper West Side, one block from Central Park's western edge."
    ],
    "Flushing–Main Street": [
        "This is the eastern terminus of its line and the end of the longest single-line journey in the Queens subway network.",
        "It serves as the gateway to one of the largest and most active Chinese-American communities in the United States."
    ],
    "Grand Central–42nd Street": [
        "The shuttle connecting this station to Times Square is one of the most heavily trafficked stretches of track in the world.",
        "Despite sharing a name with one of NYC's most famous buildings, this station is entirely underground and separate from the terminal above."
    ],
    "Times Square–42nd Street": [
        "This station sits at the convergence of more lines than any other in the system, making it the busiest in the entire NYC subway.",
        "A famous mural by pop artist Roy Lichtenstein has decorated its corridors since 1994."
    ]
}

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
server = discord.Object(id=1081625448385085440)
current_station = None

bot = commands.Bot(command_prefix="m!", intents=intents)

@tasks.loop(minutes=5)
async def send_interval_message():
    global current_station
    channel = bot.get_channel(1477473312291553453)
    current_station = random.choice(list(station_data.keys()))
    await channel.send("A wild metro station appeared.")
    print(f"Spawned {current_station}!")

async def station_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=station, value=station)
        for station in list(station_data.keys())
        if current.lower() in station.lower()
    ]

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

@bot.tree.command(name="guess", description="Take a stab at capturing a spawned station.")
@app_commands.autocomplete(station_name=station_autocomplete)
async def guess(interaction: discord.Interaction, station_name: str):
    global current_station
    if current_station:
        if station_name == current_station:
            caught = current_station
            current_station = None
            await interaction.response.send_message(f"{interaction.user.mention} guessed correctly and collected **{caught}**!")
        else:
            await interaction.response.send_message(f"{interaction.user.mention} Wrong station!")
    else:
        await interaction.response.send_message("Doesn't seem like there's a station spawned right now. Try again later!", ephemeral=True)
        

bot.run(TOKEN)