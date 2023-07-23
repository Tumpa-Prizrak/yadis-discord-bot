from discord.ext.commands import Bot  # type: ignore
from discord import Intents
from typing import Dict, Tuple, Any
from logging import Logger
from api import logger
import os
from api.tools import load_extensions


class Yadis(Bot):
    """The Yadis bot class inherits from Bot discord.py.
    
    Overrides methods to configure and run the bot.
    """
    def __init__(
        self,
        command_prefix: str,
        intents: Intents,
        token: str,
        *args: Tuple[Any],
        **kwargs: Dict[str, Any],
    ) -> None:
        """Bot initialisation.
        
        :param command_prefix: Command prefix 
        :param intents: Bot intents
        :param token: Bot token
        """
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
    

    async def sync_slash(self):
        for guild in self.guilds:
            self.tree.copy_global_to(guild=guild)
            self.logger.info(f"Copying slashes to {guild.name}")
        
        await self.tree.sync(guild=None)
        self.logger.info("Slash commands synced!")

    
    async def setup_hook(self) -> None:
        """Configuring the bot before launching it.
        
        Loading command and event extensions.
        """
        for category in os.listdir("bot/cogs"):
            obj = f"bot/cogs/{category}"
            if os.path.isfile(obj): continue

            await load_extensions(self, obj, "cog_")
        
        await load_extensions(self, "bot/events", "event_")

        await self.sync_slash()

    async def on_ready(self) -> None:
        """Actions at bot startup.
        
        Readiness and delay logging.
        """
        self.logger.info(f"Bot is ready! latency: {round(self.latency, 3)}")

    def run(self, token: str | None = None) -> None:  # type: ignore
        """Bot startup.
        
        :param token: Bot token, by default taken from attribute.
        """
        super().run(token or self.token, reconnect=True)
