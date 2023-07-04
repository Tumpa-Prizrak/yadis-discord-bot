from discord.ext import commands
from src.models.bot import Yadis
import discord
from src.database import api
from src.models import discord as DiscordModels

class EventsCog(commands.Cog):
    def __init__(self, client: commands.Bot):
       self.client = client
       self.temp_channels = []
    
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if before is None:
            guild: DiscordModels.Guild = await api.get_guild(guild=member.guild)

            if after.channel == guild.custom_voice_entery:
                channel = await self._create_temp_voice_channel(guild, member)
                await member.move_to(channel)
        elif after is None:
            if before.channel.id in self.temp_channels and not before.channel.members:
                await self._delete_temp_voice_channel(before.channel.id)

    async def _create_temp_voice_channel(self, guild: DiscordModels.Guild, member: discord.Member) -> discord.VoiceChannel:
        channel: discord.VoiceChannel = await guild.create_voice_channel(f"{member.display_name}'s channel")
        channel.edit(user_limit=1, category=guild.custom_voice_entery.category)
        self.temp_channels.append(channel.id)
        return channel
    
    async def _delete_temp_voice_channel(self, channel: discord.VoiceChannel):
        await channel.delete()
        self.temp_channels.remove(channel.id)

async def setup(client: Yadis):
    await client.add_cog(EventsCog(client))
