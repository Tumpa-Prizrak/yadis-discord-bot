from discord.ext.commands import Bot
from typing import Optional
from src import custom_logs
from asyncio import run as async_run
from os import listdir
from src.models import error
from discord import Intents


class Yadis(Bot):
    def __init__(
        self,
        debug_channel_id: int,
        intents: int,
        token: Optional[str] = None,
        *args,
        **kwargs,
    ):
        super().__init__(
            command_prefix="None",
            case_insensitive=False,
            strip_after_prefix=True,
            help_command=None,
            intents=Intents(intents),
            *args,
            **kwargs,
        )
        self.token = token
        self.debug_channel = self.get_channel(debug_channel_id)
        self.logger = custom_logs.Logger("Bot", self)
        self.commands_logger = custom_logs.Logger("Commands", self)

    async def on_ready(self):
        await self.logger.success("Ready!", to_file=False)

    def run(self, token: Optional[str] = None):       
        async_run(
            self.logger.success("Locked and loaded!", to_file=False, to_channel=False)
        )
        async_run(self.logger.info("Starting...", to_file=False, to_channel=False))
        super().run(token or self.token)  # type: ignore

    """async def on_command_error(self, _, exception: Exception):
        await self.commands_logger.error(str(exception))

    async def on_error(self, event, *args, **kwargs):
        print(event)
        print(args)
        print(kwargs)
        await self.commands_logger.error(
            f"{event} {' '.join(args)} {' '.join(map(lambda x, y: f'{x}={y}', kwargs.items()))}"
        )"""

    async def setup_hook(self):
        print("\nCogs")
        for category in listdir("src/cogs"):
            for cog in listdir(f"src/cogs/{category}"):
                await self._load_cog(f"src.cogs.{category}.{cog[:-3]}")
        print("[END] Cogs\n")
        
        print("Events")
        for cog in listdir(f"src/events/"):
            await self._load_cog(f"src.events.{cog[:-3]}")
        print("[END] Events\n")

    async def _load_cog(self, path: str):
        if path.endswith(".__pycach"):
            return
        try:
            await self.load_extension(path)
            await self.logger.success(
                f"{path} loaded!",
                to_channel=False,
                to_file=False,
            )
        except Exception as e:
            await self._log_exception_while_loading_cog(e.args[0], path)

    async def _log_exception_while_loading_cog(self, e: str, path: str):
        if len(s := e.split(": ")) >= 2:
            e = ": ".join(s[1:])
        if any(filter(lambda x: x.__name__ in e, error._warnings)):  # type: ignore
            log_func = self.logger.warning
        else:
            log_func = self.logger.error
        await log_func(f"{e} while loading {path}", to_channel=False)
