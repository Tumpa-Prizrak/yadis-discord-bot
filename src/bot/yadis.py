from discord.ext.commands import Bot
from discord import Intents
from api.logger import setup_logger, get_file_formatter, get_file_handler
from logging import Logger, INFO


class Yadis(Bot):
    def __init__(
        self, command_prefix: str, intents: Intents, token: str, *args, **kwargs
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
        self.logger: Logger = setup_logger()

    async def on_ready(self):
        self.logger.info(f"Bot is ready! latency: {round(self.latency, 4)}")

    def run(self, token: str | None = None) -> None:
        super().run(
            token or self.token,
            reconnect=True,
            log_level=INFO,  # FIXME: several logging
            log_handler=get_file_handler(),
            log_formatter=get_file_formatter(),
            root_logger=True,
        )
