import discord
from discord.ext import commands
from typing import Optional
from src import custom_logs
from asyncio import run as async_run
from os import listdir
from src.models import error


class Yadis(commands.Bot):
    """The main bot class."""
    
    def __init__(
        self,
        debug_channel_id: int,
        intents: int,
        token: Optional[str] = None,
        *args,
        **kwargs,
    ):
        """Initialize the Yadis bot.
        
        Args:
            debug_channel_id (int): The ID of the debug channel.
            intents (int): The Discord intents.
            token (Optional[str], optional): The bot token. Defaults to None.
        """
        ...

    async def on_ready(self):
        """Called when the bot is ready."""
        ...

    def run(self, token: Optional[str] = None):
        """Run the bot.
        
        Args:
            token (Optional[str], optional): The bot token. Defaults to entered token.
        """
        ...

    async def setup_hook(self):
        """Set up the bot's cogs."""
        ...
