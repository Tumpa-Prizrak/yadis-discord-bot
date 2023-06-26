import discord
from discord.ext import commands
from typing import Optional
from src import custom_logs
from asyncio import run as async_run
from os import listdir
from src.models import error


class Yadis(commands.Bot):
    def __init__(
        self,
        debug_channel_id: int,
        intents: int,
        token: Optional[str] = None,
        *args,
        **kwargs,
    ):
        super().__init__(
            case_insensitive=False,
            strip_after_prefix=True,
            help_command=None,
            intents=discord.Intents(intents),
            *args,
            **kwargs,
        )
        self.token = token
        self.debug_channel = self.get_channel(debug_channel_id)
        self.logger = custom_logs.Logger("Bot", self)
        self.commands_logger = custom_logs.Logger("Commands", self)

    async def on_ready(self):
        await self.logger.sucsess("Ready!", to_file=False)

    def run(self, token: Optional[str] = None):
        async_run(
            self.logger.sucsess("Locked and loaded!", to_file=False, to_channel=False)
        )
        async_run(self.logger.info("Starting...", to_file=False, to_channel=False))
        super().run(token or self.token)

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
                try:
                    if cog.endswith(".py") and not cog.startswith("nc_"):
                        await self.load_extension(f"src.cogs.{category}.{cog[:-3]}")
                        await self.logger.sucsess(
                            f"cog {category}.{cog[-3]} loaded!", to_channel=False, to_file=False
                        )
                except Exception as e:
                    e = e.args[0]
                    if len(s := e.split(": ")) >= 2:
                        e = ": ".join(s[1:])
                    if any(filter(lambda x: x.__name__ in e, error._warnings)):
                        func = self.logger.warning
                    else:
                        func = self.logger.error
                    await func(f"{e} while loading cog {cog}", to_channel=False)
        print("[END] Cogs\n")
