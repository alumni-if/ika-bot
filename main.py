import discord
import os
import math

from dotenv import load_dotenv

import helpers.log as log
from core.custom_client import MyCustomClient

load_dotenv()

intents = discord.Intents.default()
intents.members = bool(os.getenv('INTENTS_MEMBER', 'True'))
intents.message_content =  bool(os.getenv('INTENTS_MESSAGE_CONTENT', 'False')) # no need hear all message from user. make a lot of requests
guild_id = os.getenv('DEVELOPMENT_GUILD_ID')

client = MyCustomClient(guild_id=os.getenv('DEVELOPMENT_GUILD_ID'), command_prefix='?', intents=intents)

@client.tree.command(name='ping', description='Check the bot\'s ping', guild=client.guild)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Ping Server is: {round(client.latency * 1000)}ms')

client.run(
    os.getenv('MTI5MTg5OTc3NTMyMjQyNzQyMw'),
    log_handler=log.console_handler,
)