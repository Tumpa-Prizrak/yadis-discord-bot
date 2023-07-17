from api.database import orm
import discord
from discord.ext.commands import Bot  # type: ignore
from models import discord_models
from typing import List


def get_guild(*, bot: Bot, guild: discord.Guild) -> discord_models.Guild:
    if (guild_data := orm.get_guild(bot, guild.id)) is None:
        orm.auto_add_guild(guild)
        guild_data = orm.get_guild(bot, guild.id)
    
    if (settings_data := orm.get_settings(bot, guild.id)) is None:
        orm.add_settings(guild.id)
        settings_data = orm.get_settings(bot, guild.id)

    assert guild_data is not None and settings_data is not None

    return discord_models.Guild.from_discord(guild, settings_data, is_blacklisted=guild_data.blacklisted)    


def get_guild_by_id(*, bot: Bot, guild_id: int) -> discord_models.Guild:
    guild = bot.get_guild(guild_id)
    if guild is None:
        raise ValueError("guild is not found")

    return get_guild(bot=bot, guild=guild)


def get_guild_by_owner(*, bot: Bot, owner_id: int) -> discord_models.Guild:
    guilds: List[discord.Guild] = bot.get_user(owner_id).mutual_guilds  # type: ignore
    for guild in guilds:
        if guild.owner_id == owner_id:
            return get_guild(bot=bot, guild=guild)
    raise ValueError(f"User {owner_id} doesn't own any mutal guilds")
