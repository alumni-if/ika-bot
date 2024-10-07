import discord
from discord.ext import commands
from discord import app_commands

async def setup(bot: commands.Bot):
    await bot.add_cog(Ika(bot))

class Ika(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot
    
    @app_commands.command(name='ika_sync', description='Sync From SpreadSheet and Local Database of List Not Fill Form')
    async def ika_member(self, interaction: discord.Interaction):
        members = [member for member in interaction.guild.members if not member.bot]
        await interaction.response.send_message('\n'.join([f'{member.mention} - {member.id} - {member.name} - {member.display_name}' for member in members]))