import discord

class MyCustomClient(discord.Client):
    """
    Custom Client

    This is the class which inherits discord.Client, and
    override two methods: on_ready and on_message.
    """
    async def on_ready(self):
        """
        Called after the Client is connected and ready, successfully logged in and
        has completed the initial handshake with the Discord API.

        Prints to console the logged on user.
        """
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        """
        Called when a Message is created and sent.

        Prints to console the message author and content.
        """
        # print(f'Message from {message.author}: {message.content}')
        pass

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



