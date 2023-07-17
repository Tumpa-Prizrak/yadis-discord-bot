from models.dataclasses import Guild, Settings
import discord
from api.database import tools, enums
from discord.ext.commands import Bot  # type: ignore


### Guild ###

def get_guild(bot: Bot, guild_id: int) -> Guild | None:
    with tools.DatabaseConnection() as db:
        data = db.read("SELECT * FROM guild WHERE discord_id = ?", guild_id, mode=enums.DBFormat.One)
        if data is None:
            return None
        return Guild(bot, *data)

def auto_add_guild(guild: discord.Guild) -> None:
    assert guild.owner_id is not None

    add_guild(guild.id, guild.owner_id)

def add_guild(guild_id: int, owner_id: int) -> None:
    with tools.DatabaseConnection() as db:
        db.write("INSERT INTO guild (discord_id, owner_id) VALUES (?, ?)", guild_id, owner_id, raise_errors=True)


### Settings ###

def get_settings(bot: Bot, discord_id: int) -> Settings | None:
    with tools.DatabaseConnection() as db:
        data = db.read("SELECT * FROM settings WHERE discord_id = ?", discord_id, mode=enums.DBFormat.One)
        if data is None:
            return None
        return Settings(bot, *data)

def add_settings(discord_id: int) -> None:
    with tools.DatabaseConnection() as db:
        db.write("INSERT INTO settings (discord_id) VALUES (?)", discord_id, raise_errors=True)
