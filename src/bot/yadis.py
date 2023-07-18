from discord.ext.commands import Bot  # type: ignore
from discord import Intents
from typing import Dict, Tuple, Any
from logging import Logger
from api import logger
import os
from api.tools import load_extensions


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
    
    async def setup_hook(self) -> None:
        for category in os.listdir("bot/cogs"):
            obj = f"bot/cogs/{category}"
            if os.path.isfile(obj): continue

            await load_extensions(self, obj, "cog_")
        
        await load_extensions(self, "bot/events", "event_")


    async def on_ready(self) -> None:
        self.logger.info(f"Bot is ready! latency: {round(self.latency, 3)}")

    def run(self, token: str | None = None) -> None:  # type: ignore
        super().run(token or self.token, reconnect=True)
