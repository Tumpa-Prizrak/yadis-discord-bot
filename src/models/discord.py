import discord
import typing


class Guild:
    custom_voice_entry: typing.Optional[discord.VoiceChannel]
    guild: discord.Guild

    def __init__(self, guild: discord.Guild, custom_voice_entry: typing.Optional[discord.VoiceChannel] = None) -> None:
        self.custom_voice_entry = custom_voice_entry
        self.guild = guild
