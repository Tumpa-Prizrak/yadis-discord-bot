from contextlib import suppress
from typing import Self, Callable
from models.dataclasses import Settings
import discord
import inspect


class Guild(discord.Guild):
    """Guild class that extends discord.Guild.

    Adds attributes:

    - settings: server settings object
    - is_blacklisted: blacklisted.

    Provides a from_discord method to create an instance of the
    of a class from the discord.Guild object.
    """
    settings: Settings
    is_blacklisted: bool

    @classmethod
    def from_discord(
        cls, guild: discord.Guild, settings: Settings, is_blacklisted: bool = False
    ) -> Self:
        """Creates a Guild instance from discord.Guild.

        :param guild: Discord.Guild object
        :param settings: Settings object
        :param is_blacklisted: Blacklisted

        :return: An instance of the Guild class
        """
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
