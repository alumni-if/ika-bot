import discord
import log
import math

from custom_client import MyCustomClient

DEVELOPMENT_GUILD_ID = 1291935358501781504

intents = discord.Intents.default()
intents.members = True
intents.message_content = False # no need hear all message from user. make a lot of requests

client = MyCustomClient(guild_id=DEVELOPMENT_GUILD_ID, command_prefix='?', intents=intents)

@client.tree.command(name='greeting', description='Send a greeting message', guild=client.guild)
async def greeting_command(interaction: discord.Interaction):
    await interaction.response.send_message(f'Halo {interaction.user.mention}! Selamat Datang di Server Discord IKA Informatika Universitas Mataram. Nice to meet you!')

@client.tree.command(name='phitimes', description='Phi Times with 2 arguments', guild=client.guild)
async def phitimes_command(interaction: discord.Interaction, arg1: float, arg2: float, arg3: str):
    await interaction.response.send_message(f'Phi times {arg1} times {arg2} = {math.pi * arg1 * arg2}. Greeting {arg3}')

@client.tree.command(name='allmember', description='Get all members', guild=client.guild)
async def allmember_command(interaction: discord.Interaction):
    members = []
    bots = []

    member_counter = 1
    bot_counter = 1
    
    for member in interaction.guild.members:
        if member.bot:
            bots.append(f'{bot_counter}. {member.mention} - {member.id} - {member.name} - {member.display_name}')
            bot_counter += 1
        else:
            members.append(f'{member_counter}. {member.mention} - {member.id} - {member.name} - {member.display_name}')
            member_counter += 1

    await interaction.response.send_message(f"Total members: {interaction.guild.member_count}\n\n" + 
                                            "Real user:\n" + '\n'.join(members) + "\n\n" +
                                            "Bot:\n" + '\n'.join(bots))

client.run(
    'MTI5MTg5OTc3NTMyMjQyNzQyMw.GZ3BRj.IRgesnYu5wlEg052fKjQU7GqpgNJNWRJdv8beQ',
    log_handler=log.console_handler,
)