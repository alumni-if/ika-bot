import os

async def load_cogs(bot):

    """Load all cogs in the 'cogs' directory.
    
    This function is called during the bot's startup process, and is used to load all
    cogs from the 'cogs' directory. The cogs are loaded in the order they are found in
    the directory, and each cog is loaded in the following way:

    1. The bot's load_extension method is called with the name of the cog as the
       argument.
    2. The bot's reload_extension method is called with the name of the cog as the
       argument.

    This function is a coroutine, and should be called with the await keyword.

    Docs: https://discordpy.readthedocs.io/en/stable/ext/commands/api.html#discord.ext.commands.Bot.load_extension
    """
    
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')