import discord
from discord.ext import commands
from helpers.cogs_helper import load_cogs
from cogs.commands import MyCommands

class MyCustomClient(commands.Bot):
    
    def __init__(self, guild_id, *args, **kwargs) :
        self.guild_id = guild_id
        self.guild = discord.Object(id=guild_id)
        
        # Forward all arguments, and keyword-only arguments to commands.Bot
        super().__init__(*args, **kwargs)
        
    """
    Custom Client

    This is the class which inherits discord.Client, and
    override two methods: on_ready and on_message.
    """
    async def on_ready(self):
        """
        Called after the bot is ready.

        Prints a message to console, when the bot is ready.
        Syncs all slash commands to the guild, where the bot is invited.
        Syncs all global slash commands.

        Loads all cogs from the 'cogs' directory.
        """
        
        print(f'Logged on as {self.user}!')

        # Cogs load
        await load_cogs(self)

        # Sync cogs
        try:
            synced_cogs = await self.tree.sync()
            print(f'Synced Cogs {len(synced_cogs)} command(s) to {self.guild_id}!')
        except Exception as e:
            print(f"Error syncing Cogs commands: {e}")

        # Sync our Bot commands from `@client.tree.command`
        try:
            synced = await self.tree.sync(guild=self.guild)
            print(f'Synced {len(synced)} command(s) to {self.guild_id}!')
        except Exception as e:
            print(f"Error syncing commands: {e}")
            
        # Sync our Global commands
        if False:
            try:
                synced = await self.tree.sync()
                print(f'Synced {len(synced)} global command(s)!')
            except Exception as e:
                print(f"Error syncing commands: {e}")
        
        print(f"Total Commands: {len(synced_cogs + synced)}")

    async def on_message(self, message):
        """
        Called when a Message is created and sent.

        Prints to console the message author and content.
        """
        # print(f'Message from {message.author}: {message.content}')
        if message.author == self.user:
            return
        
        if message.content.startswith('hello'):
            userId = message.author.id
            usernameDiscord = message.author.name
            await message.channel.send(f"Hello too {message.author.mention}. userid: {userId}, discord username: {usernameDiscord}")

    async def on_member_join(self, member):
        """
        Called when a Member joins a Guild.

        Sends a welcome message to the System Channel, if set. and do some other actions
        """
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

        # TODO: add some other staff for new member



