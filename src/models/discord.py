import discord
from typing import Optional


class Guild(discord.Guild):
    custom_voice_entery: Optional[discord.VoiceChannel]

    @classmethod
    def from_guild(
        cls,
        guild: discord.Guild,
        custom_voice_entry: Optional[discord.VoiceChannel] = None,
    ):
        """Construct a Guild object from a discord.Guild.

        Args:
            guild (discord.Guild): The discord.Guild to construct from.
            custom_voice_entery (Optional[discord.VoiceChannel], optional): The custom voice channel. Defaults to None.

        Returns:
            Guild: The constructed Guild object.
        """
        # FIXME still not tested and shouldn't work
        obj = cls(
            data=guild.__class__.data,
            custom_voice_entery=custom_voice_entry,
            roles=guild.roles,
            emojis=guild.emojis,
            features=guild.features,
            id=guild.id,
            name=guild.name,
            icon=guild.icon
        )
        return obj
