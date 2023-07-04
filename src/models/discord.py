import typing
from discord import (
    VoiceChannel,
    Guild as dGuild
)


class Guild:
    custom_voice_entry: typing.Optional[VoiceChannel]
    guild: dGuild

    def __init__(self, guild: dGuild, custom_voice_entry: typing.Optional[VoiceChannel] = None) -> None:
        self.custom_voice_entry = custom_voice_entry
        self.guild = guild
