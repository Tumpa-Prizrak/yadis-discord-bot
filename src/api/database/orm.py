from models.dataclasses import Guild, Settings
import discord
from api.database import tools, enums
from discord.ext.commands import Bot  # type: ignore


### Guild ###

def get_guild(bot: Bot, guild_id: int) -> Guild | None:
    """Gets the Guild object by server id in the database.

    :param bot: Bot instance
    :type bot: Bot

    :param guild_id: Server ID in Discord
    :type guild_id: int

    :return: Guild object or None
    :rtype: models.discord_models.guild.Guild | None
    """
    with tools.DatabaseConnection() as db:
        data = db.read("SELECT * FROM guild WHERE discord_id = ?", guild_id, mode=enums.DBFormat.One)
        return None if data is None else Guild(bot, *data)

def auto_add_guild(guild: discord.Guild) -> None:
    """Automatically adds the server to the database.

    :param guild: Discord server object
    :type guild: discord.Guild
    """
    assert guild.owner_id is not None

    add_guild(guild.id, guild.owner_id)

def add_guild(guild_id: int, owner_id: int) -> None:
    """Adds a server to the database manually by ID.

    :param guild_id: server ID in Discord
    :type guild_id: int

    :param owner_id: server owner ID
    :type owner_id: int
    """
    with tools.DatabaseConnection() as db:
        db.write("INSERT INTO guild (discord_id, owner_id) VALUES (?, ?)", guild_id, owner_id, raise_errors=True)


### Settings ###

def get_settings(bot: Bot, discord_id: int) -> Settings | None:
    """Gets the Settings object by discord_id from the database.
    
    :param bot: Bot instance
    :type bot: Bot
    
    :param discord_id: Server ID
    :type discord_id: int
    
    :return: Settings object or None
    :rtype: Settings | None
    """
    with tools.DatabaseConnection() as db:
        data = db.read("SELECT * FROM settings WHERE discord_id = ?", discord_id, mode=enums.DBFormat.One)
        return None if data is None else Settings(bot, *data)

def add_settings(discord_id: int) -> None:
    """Adds an entry to the settings table by discord_id
    
    :param discord_id: user or server ID
    :type discord_id: int
    """
    with tools.DatabaseConnection() as db:
        db.write("INSERT INTO settings (discord_id) VALUES (?)", discord_id, raise_errors=True)
