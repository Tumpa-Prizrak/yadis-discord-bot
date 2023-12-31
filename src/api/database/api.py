from api.database import orm
import discord
from discord.ext.commands import Bot  # type: ignore
from models import discord_models
from typing import List


def get_guild(*, bot: Bot, guild: discord.Guild) -> discord_models.Guild:
    """Gets a GuildBot object from the database.
    
    First it tries to find records by guild ID in tables 
    guild and settings.
    
    If there are no records, it creates them using the functions 
    :ref: auto_add_guild and add_settings.
    
    :param bot: Bot instance
    :type bot: Bot
    
    :param guild: Discord guild object
    :type guild: discord.Guild
    
    :return: GuildBot object
    :rtype: discord_models.Guild
    """
    if (guild_data := orm.get_guild(bot, guild.id)) is None:
        orm.auto_add_guild(guild)
        guild_data = orm.get_guild(bot, guild.id)
    
    if (settings_data := orm.get_settings(bot, guild.id)) is None:
        orm.add_settings(guild.id)
        settings_data = orm.get_settings(bot, guild.id)

    assert guild_data is not None and settings_data is not None

    return discord_models.Guild.from_discord(guild, settings_data, is_blacklisted=guild_data.blacklisted)    


def get_guild_by_id(*, bot: Bot, guild_id: int) -> discord_models.Guild:
    """Gets Guild object by guild ID.
    
    :param bot: Bot instance
    :type bot: Bot
    
    :param guild_id: guild ID
    :type guild_id: int
    
    :return: Guild object
    :rtype: discord_models.Guild
    
    :raises ValueError: If guild not found
    """
    guild = bot.get_guild(guild_id)
    if guild is None:
        raise ValueError("guild is not found")

    return get_guild(bot=bot, guild=guild)


def get_guild_by_owner(*, bot: Bot, owner_id: int) -> discord_models.Guild:
    """Gets a Guild object by owner ID.
    
    :param bot: Bot instance
    :type bot: Bot
    
    :param owner_id: Owner ID
    :type owner_id: int
    
    :return: Guild object
    :rtype: discord_models.Guild
    
    :raises ValueError: If guild not found
    """
    guilds: List[discord.Guild] = bot.get_user(owner_id).mutual_guilds  # type: ignore
    for guild in guilds:
        if guild.owner_id == owner_id:
            return get_guild(bot=bot, guild=guild)
    raise ValueError(f"User {owner_id} doesn't own any mutal guilds")
