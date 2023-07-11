from typing import Optional, Union

from discord import Guild as dGuild
from discord import NotFound, User

from src.database.enums import DBFormat
from src.database.tools import DatabaseConnection
from src.models.bot import Yadis
from models.discord.guild import Guild


async def get_guild(
    bot: Yadis,
    *,
    owner: Optional[Union[User, int]] = None,
    guild: Optional[Union[dGuild, int]] = None
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
    return Guild(guild, voice_channel)


async def add_guild(guild: Union[dGuild, Guild]):
    if isinstance(guild, dGuild):
        guild = Guild(guild, False, None)
    await _add_guild(guild)


async def _add_guild(guild: Guild):
    with DatabaseConnection() as db:
        db.write(
            "INSERT INTO Guild (guild_id, owner, custom_voice_entery_id, is_blacklisted) VALUES (?, ?, ?, ?)",
            guild.guild.id,
            guild.guild.owner_id,
            guild.custom_voice_entry.id if guild.custom_voice_entry is not None else None,
            guild.is_blacklisted
        )


async def _resolve_user(bot: Yadis, user_id):
    if isinstance(user_id, int):
        user = await bot.fetch_user(user_id)
        if user is None:
            raise ValueError("Owner is not found")
    else:
        user = user_id
    return user


async def _get_guild_by_owner(bot: Yadis, owner: User):
    with DatabaseConnection() as db:
        db_data = db.read("SELECT * FROM guild WHERE owner = ?", owner.id, mode=DBFormat.One)
        if not db_data:
            raise ValueError("Guild not found in the database. You should add it first")
    return await bot.fetch_guild(db_data[1])


async def _resolve_guild(bot: Yadis, guild_id: int):
    return (  # I love sourcery (no)
        await bot.fetch_guild(guild_id) if isinstance(guild_id, int) else guild_id
    )


async def _get_voice_channel(bot: Yadis, guild: dGuild | int):
    with DatabaseConnection() as db:
        db_data = db.read("SELECT * FROM guild WHERE guild_id=?", guild.id if isinstance(guild, dGuild) else guild, mode=DBFormat.One)
    try:
        voice_channel = await bot.fetch_channel(db_data[4])
    except NotFound:
        voice_channel = None
    return voice_channel
