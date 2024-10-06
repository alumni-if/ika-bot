import discord
import log
import math

from custom_client import MyCustomClient

DEVELOPMENT_GUILD_ID = 1291935358501781504

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = MyCustomClient(guild_id=DEVELOPMENT_GUILD_ID, command_prefix='?', intents=intents)

@client.tree.command(name='greeting', description='Send a greeting message', guild=client.guild)
async def greeting_command(interaction: discord.Interaction):
    await interaction.response.send_message(f'Halo {interaction.user.mention}! Selamat Datang di Server Discord IKA Informatika Universitas Mataram. Nice to meet you!')

@client.tree.command(name='phitimes', description='Phi Times with 2 arguments', guild=client.guild)
async def phitimes_command(interaction: discord.Interaction, arg1: float, arg2: float, arg3: str):
    await interaction.response.send_message(f'Phi times {arg1} times {arg2} = {math.pi * arg1 * arg2}. Greeting {arg3}')

client.run(
    'MTI5MTg5OTc3NTMyMjQyNzQyMw.GZ3BRj.IRgesnYu5wlEg052fKjQU7GqpgNJNWRJdv8beQ',
    log_handler=log.console_handler,
)