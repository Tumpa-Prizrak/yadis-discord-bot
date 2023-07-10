import typing

from discord import Guild as dGuild
from discord import VoiceChannel


class Guild:
    custom_voice_entry: typing.Optional[VoiceChannel]
    is_blacklisted: bool
    guild: dGuild

    def __init__(
        self,
        guild: dGuild,
        is_blacklisted: bool | int,
        custom_voice_entry: typing.Optional[VoiceChannel] = None,
    ) -> None:
        self.guild = guild
        self.is_blacklisted = bool(is_blacklisted)
        self.custom_voice_entry = custom_voice_entry
