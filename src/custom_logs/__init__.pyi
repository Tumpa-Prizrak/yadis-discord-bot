import colorama
import datetime
from src import config
from discord.ext.commands import Bot
from discord import Embed
from functools import partialmethod
import os

log_data = config.load_config(config.Configs.logger)
bot_info = config.load_config(config.Configs.bot_info)

class Logger:
    """A logger class."""

    def __init__(self, source: str = "", bot: Bot = None):
        """Initialize the Logger.

        Args:
            source (str, optional): The source of the logs. Defaults to "".
            bot (Bot, optional): The bot object. Defaults to None.
        """
        ...
    def format(self, level: str, message: str, level_color: colorama.Fore = None):
        """Format a log message.

        Args:
            level (str): The log level.
            message (str): The log message.
            level_color (colorama.Fore, optional): The color of the log level. Defaults to None.

        Returns:
            str: The formatted log message.
        """
        ...
    def format_embed(self, level_color: colorama.Fore, level: str, message: str):
        """Format a log message as an embed.

        Args:
            level_color (colorama.Fore): The color of the log level.
            level (str): The log level.
            message (str): The log message.

        Returns:
            Embed: The log message embed.
        """
        ...
    @staticmethod
    def get_file():
        """Get the log file path.

        Returns:
            str: The log file path.
        """
        ...
    def write_to_file(self, level: str, message: str):
        """Write a log message to file.

        Args:
            level (str): The log level.
            message (str): The log message.
        """
        ...
    async def log(
        self,
        message: str,
        *,
        level_color: colorama.Fore,
        level: str,
        to_file: bool = True,
        to_channel: bool = True,
    ):
        """Log a message.

        Args:
            message (str): The log message.
            level_color (colorama.Fore): The color of the log level.
            level (str): The log level.
            to_file (bool, optional): Whether to log to file. Defaults to True.
            to_channel (bool, optional): Whether to log to the debug channel. Defaults to True.
        """
        ...
    error = partialmethod(log, level_color=colorama.Fore.RED, level="ERROR")
    warning = partialmethod(
        log, level_color=colorama.Fore.LIGHTYELLOW_EX, level="WARNING"
    )
    info = partialmethod(log, level_color=colorama.Fore.LIGHTGREEN_EX, level="INFO")
    success = partialmethod(log, level_color=colorama.Fore.GREEN, level="SUCCESS")
