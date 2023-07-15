from dataclasses import dataclass
import discord
import typing
from discord.ext import commands


@dataclass
class Database:  # Config only
    database_path: str
    database_schema: str


"""
@dataclass
class Logger:
    log_format: str
    dt_format: str
    filename_format: str
"""


@dataclass
class BotInfo:  # Config only
    token: str
    prefix: str
    intents: int

@dataclass
class Settings:  # Database only
    rowid: int
    guild: discord.Guild
    blacklisted: typing.List[discord.User]
    custom_voice_entery: discord.VoiceChannel | None
    welcome_channel: discord.TextChannel | None
    welcome_messages: typing.List[str]
    verification_role: discord.Role | None
    mod_roles: typing.List[discord.Role]
    admin_roles: typing.List[discord.Role]

    def __init__(self, **kwargs: typing.Dict[str, typing.Any]):
        bot: commands.Bot | None = kwargs.get("bot", None)  # type: ignore
        if not isinstance(bot, commands.Bot):
            raise RuntimeError("You should specify 'bot' attribute")

        self.rowid = kwargs.get("rowid", 0)  # type: ignore
        self.guild = bot.get_guild(kwargs.get("discord_id", 0))  # type: ignore
        self.blacklisted = [bot.get_user(x) for x in kwargs.get("blacklisted", "").split()]  # type: ignore
        self.custom_voice_entery = bot.get_channel(kwargs.get("custom_voice_entery", 0)) or None  # type: ignore
        self.welcome_channel = bot.get_channel(kwargs.get("welcome_channel", 0)) or None  # type: ignore
        self.welcome_messages = kwargs.get("welcome_messages", "").split("\n")  # type: ignore
        self.verification_role = bot.get_role(kwargs.get("verification_role", 0)) or None  # type: ignore
        self.mod_roles = [bot.get_role(x) for x in kwargs.get("mod_roles", "").split()]  # type: ignore
        self.admin_roles = [bot.get_role(x) for x in kwargs.get("admin_roles", "").split()] # type: ignore
        
        if self.guild is None:
            raise ValueError("Guild is not found")
