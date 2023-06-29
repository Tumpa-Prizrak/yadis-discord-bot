import discord
from typing import Optional


class Guild(discord.Guild):
    custom_voice_entery: Optional[discord.VoiceChannel]

    @classmethod
    def fromGuild(
        cls,
        guild: discord.Guild,
        custom_voice_entery: Optional[discord.VoiceChannel] = None,
    ):
        """Construct a Guild object from a discord.Guild.

        Args:
            guild (discord.Guild): The discord.Guild to construct from.
            custom_voice_entery (Optional[discord.VoiceChannel], optional): The custom voice channel. Defaults to None.

        Returns:
            Guild: The constructed Guild object.
        """
        # TODO rewrite
        obj = cls(data=guild.)
        obj.roles = guild.roles
        obj.channels = guild.channels
        obj.members = guild.members
        obj.custom_voice_entery = custom_voice_entery
        return obj
