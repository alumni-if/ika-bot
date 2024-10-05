import discord
import log

from discord.ext import commands
from custom_client import MyCustomClient as Client



intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = Client(intents=intents)

client.run(
    'MTI5MTg5OTc3NTMyMjQyNzQyMw.GZ3BRj.IRgesnYu5wlEg052fKjQU7GqpgNJNWRJdv8beQ',
    log_handler=log.console_handler,
)