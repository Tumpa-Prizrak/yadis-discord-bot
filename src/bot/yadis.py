from discord.ext.commands import Bot  # type: ignore
from discord import Intents
from logging import Logger, getLogger
from typing import Dict, Tuple, Any

class Yadis(Bot):
    def __init__(
        self, command_prefix: str, intents: Intents, token: str, *args: Tuple[Any], **kwargs: Dict[str, Any]
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
        self.logger: Logger = getLogger("discord.bot")

    async def on_ready(self) -> None:
        self.logger.info(f"Bot is ready! latency: {round(self.latency, 3)}")

    def run(self, token: str | None = None) -> None:  # type: ignore
        super().run(
            token or self.token,
            reconnect=True
        )
    
    def getLogger(self):
        pass
