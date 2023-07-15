from typing import Self
from models.dataclasses import Settings
import discord

class Guild(discord.Guild):
    settings: Settings
    is_blacklisted: bool

    @classmethod
    def from_discord(cls, guild: discord.Guild, settings: Settings, is_blacklisted: bool = False) -> Self:
        obj: Self = cls.__new__(cls)

        obj.__dict__ = guild.__dict__
        obj.settings = settings
        obj.is_blacklisted = is_blacklisted

        return obj
