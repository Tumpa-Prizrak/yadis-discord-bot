from src.database.tools import DatabaseConnection
from src.database.enums import DBFormat
from src.models import discord as discordModels
import discord
from typing import Optional
from src.models.bot import Yadis

async def getGuild(
    bot: Yadis, 
    *, 
    owner: Optional[discord.User | int], 
    guild: Optional[int | discord.Guild]
):
    if owner is not None and guild is not None:
        raise ValueError("You must specify either owner or guild")

    if owner is not None:
        owner = await _resolve_user(bot, owner)
        guild = await _get_guild_by_owner(bot, owner)
    elif guild is not None:
        guild = await _resolve_guild(bot, guild)
    else:
        raise ValueError("You must specify either owner or guild")

    voice_channel = await _get_voice_channel(bot, guild)
    return discordModels.Guild.fromGuild(guild, voice_channel)

async def _resolve_user(bot, user_id):
    if isinstance(user_id, int):
        user = await bot.fetch_user(user_id)
        if user is None:
            raise ValueError("Owner is not found")
    else:
        user = user_id
    return user

async def _get_guild_by_owner(bot, owner):
    with DatabaseConnection() as db:
        db_data = db.read("SELECT * FROM guild WHERE owner = ?", owner.id, mode=DBFormat.One)
        if not db_data:
            raise ValueError("Guild not found in the database. You should add it first")
    return await bot.fetch_guild(db_data[1])

async def _resolve_guild(bot, guild_id):
    if isinstance(guild_id, int):
        guild = await bot.fetch_guild(guild_id)
    else:
        guild = guild_id
    return guild  

async def _get_voice_channel(bot, guild):
    """
    И тут доки
    """
    with DatabaseConnection() as db:
        db_data = db.read("SELECT * FROM guild WHERE guild_id=?", guild.id, mode=DBFormat.One)
    try:
        voice_channel = await bot.fetch_channel(db_data[4])
    except discord.NotFound:
        voice_channel = None
    return voice_channel
