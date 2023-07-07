import datetime
import os
from functools import partialmethod
from typing import Optional

import colorama
from discord import Embed
from discord.ext.commands import Bot
from src.models.config import Logger as logger, BotInfo

from src import config

log_data = config.load_config(config.Configs.logger)
bot_info = config.load_config(config.Configs.bot_info)


class Logger:
    def __init__(self, source: str = "", bot: Optional[Bot] = None):
        self.source = source
        self.bot = bot

    def format(self, level: str, message: str, level_color: Optional[colorama.Fore] = None):  # type: ignore
        assert isinstance(log_data, logger)
        return log_data.log_format.format(
            **{
                "dt": datetime.datetime.now().strftime(log_data.dt_format),
                "source": self.source,
                "level": level,
                "message": message,
                "dt_color": config.pyconfig.Colors.dt_color
                if level_color is not None
                else None,
                "source_color": config.pyconfig.Colors.source_color
                if level_color is not None
                else None,
                "level_color": level_color if level_color is not None else "",
                "reset": config.pyconfig.Colors.reset
                if level_color is not None
                else None,
            }
        )

    def format_embed(self, level_color: colorama.Fore, level: str, message: str):  # type: ignore
        return Embed(
            title=self.source,
            color=config.pyconfig.to_dscolor(level_color),
            description=f"{level.upper()} {message.lower()}",
        )

    @staticmethod
    def get_file():
        assert isinstance(log_data, logger)
        return f'logs/{datetime.datetime.now().strftime(log_data.filename_format)}'

    def write_to_file(self, level: str, message: str):
        path = self.get_file()
        if not os.path.exists(path):
            with open(self.get_file(), "a") as f:
                f.write(
                    f"Log for {path.split('/')[-1].split('.')[0].replace('-', ' ')}"
                )
        with open(self.get_file(), "a") as f:
            f.write(f"\n{self.format(level, message).replace('None', '')}")

    async def log(
        self,
        message: str,
        *,
        level_color: colorama.Fore,  # type: ignore
        level: str,
        to_file: bool = True,
        to_channel: bool = True,
    ):
        assert isinstance(bot_info, BotInfo)
        print(self.format(level, message, level_color))
        if to_file:
            self.write_to_file(level, message)
        if to_channel and self.bot is not None:
            try:
                await self.bot.get_channel(bot_info.get("debug_channel_id", 0)).send(  # type: ignore
                    embed=self.format_embed(level_color, level, message)
                )
            except AttributeError:
                await self.error(
                    message=f"Channel {bot_info.debug_channel_id} is not found",
                    to_channel=False,
                )

    error = partialmethod(log, level_color=colorama.Fore.RED, level="ERROR")
    warning = partialmethod(
        log, level_color=colorama.Fore.LIGHTYELLOW_EX, level="WARNING"
    )
    info = partialmethod(log, level_color=colorama.Fore.LIGHTGREEN_EX, level="INFO")
    success = partialmethod(log, level_color=colorama.Fore.GREEN, level="SUCCESS")
