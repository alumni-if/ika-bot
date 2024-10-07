import discord
import math
from discord.ext import commands
from discord import app_commands

class MyCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # def cog_check(self, ctx):
    #   # source: https://stackoverflow.com/a/67386295
    #   # Docs: https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Cog.cog_check
    #   return ctx.guild.id == self.bot.guild_id

    # @app_commands is slashCommand generator.
    @app_commands.command(name='greeting', description='Send a greeting message')
    async def greeting(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Halo {interaction.user.mention}! Selamat Datang di Server Discord IKA Informatika Universitas Mataram. Nice to meet you!')

    @app_commands.command(name='phitimes', description='Phi Times with 2 arguments')
    async def phitimes(self, interaction: discord.Interaction, arg1: float, arg2: float, greeting_msg: str):
        await interaction.response.send_message(f'Phi times {arg1} times {arg2} = {math.pi * arg1 * arg2}. Greeting {greeting_msg}')

    @app_commands.command(name='allmember', description='Get all members')
    async def allmember(self, interaction: discord.Interaction):
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



# Setup function to load the cog
async def setup(bot):
    """Setup function to load the cog, given as follows:

    This function is called by discord.py when adding the cog to a bot. It
    adds the cog to the bot.
    
    this is the entry point for load_extension()

    Docs: https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot.add_cog
    """

    # someone talk about why guild/guilds in `add_cog()` doesnt work
    # source; https://github.com/Rapptz/discord.py/issues/7657
    # and this shit solve give some guide: https://www.pythondiscord.com/pages/guides/python-guides/app-commands/
    await bot.add_cog(MyCommands(bot))