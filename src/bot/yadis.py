from discord.ext.commands import Bot  # type: ignore
from discord import Intents
from typing import Dict, Tuple, Any
from logging import Logger
from api import logger
from api.database import api


class Yadis(Bot):
    def __init__(
        self,
        command_prefix: str,
        intents: Intents,
        token: str,
        *args: Tuple[Any],
        **kwargs: Dict[str, Any],
    ) -> None:
        super().__init__(
            command_prefix,
            help_command=None,
            description=None,
            intents=intents,
            *args,
            **kwargs,
        )
        self.token: str = token
        self.logger: Logger = logger.setup_logger()

    async def on_ready(self) -> None:
        self.logger.info(f"Bot is ready! latency: {round(self.latency, 3)}")
        for guild in self.guilds:
            print(api.get_guild(bot=self, guild=guild).name)

    def run(self, token: str | None = None) -> None:  # type: ignore
        super().run(token or self.token, reconnect=True)
