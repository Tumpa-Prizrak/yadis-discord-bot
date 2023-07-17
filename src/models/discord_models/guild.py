from contextlib import suppress
from typing import Self, Callable
from models.dataclasses import Settings
import discord
import inspect


class Guild(discord.Guild):
    settings: Settings
    is_blacklisted: bool

    @classmethod
    def from_discord(
        cls, guild: discord.Guild, settings: Settings, is_blacklisted: bool = False
    ) -> Self:
        obj: Self = cls.__new__(cls)

        for k, v in inspect.getmembers(guild):
            if k.startswith("__"): continue
            if isinstance(v, Callable): continue
            with suppress(AttributeError):
                obj.__setattr__(k, v)
                # print(f"{k}: {v}")

        obj.settings = settings
        obj.is_blacklisted = is_blacklisted

        return obj
