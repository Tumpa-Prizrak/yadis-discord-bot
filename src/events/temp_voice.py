from discord import Member, VoiceChannel, VoiceState
from discord.ext.commands import Bot, Cog

from src.database import api
from src.models.bot import Yadis
from models.discord.guild import Guild


class EventsCog(Cog):
    def __init__(self, client: Bot):
        self.client = client
        self.temp_channels = []

    async def on_voice_state_update(
        self, member: Member, before: VoiceState, after: VoiceState
    ):
        if before is None:
            guild: DiscordModels.Guild = await api.get_guild(bot=self.client, guild=member.guild)  # type: ignore

            if after.channel == guild.custom_voice_entery:  # type: ignore
                channel = await self._create_temp_voice_channel(guild, member)
                await member.move_to(channel)
        elif after is None:
            if before.channel.id in self.temp_channels and not before.channel.members:  # type: ignore
                await self._delete_temp_voice_channel(before.channel.id)  # type: ignore

    async def _create_temp_voice_channel(
        self, guild: Guild, member: Member
    ) -> VoiceChannel:
        channel: VoiceChannel = await guild.guild.create_voice_channel(
            f"{member.display_name}'s channel"
        )
        channel.edit(user_limit=1, category=guild.custom_voice_entery.category)  # type: ignore
        self.temp_channels.append(channel.id)
        return channel

    async def _delete_temp_voice_channel(self, channel: VoiceChannel):
        await channel.delete()
        self.temp_channels.remove(channel.id)


async def setup(client: Yadis):
    await client.add_cog(EventsCog(client))
