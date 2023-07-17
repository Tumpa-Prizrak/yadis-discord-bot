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

    def __init__(
        self,
        bot: commands.Bot,
        rowid: int,
        discord_id: int,
        blacklisted: str,
        custom_voice_entery: int | None,
        welcome_channel: int | None,
        welcome_messages: str,
        verification_role: int | None,
        mod_roles: str,
        admin_roles: str,
    ):
        
        self.rowid = rowid
        self.guild = bot.get_guild(discord_id)  # type: ignore
        if self.guild is None:
            raise ValueError("Guild is not found")
        self.blacklisted = [bot.get_user(int(x)) for x in blacklisted.split()]  # type: ignore
        self.custom_voice_entery = bot.get_channel(custom_voice_entery)  # type: ignore
        self.welcome_channel = bot.get_channel(welcome_channel)  # type: ignore
        self.welcome_messages = welcome_messages.split("\n")
        self.verification_role = self.guild.get_role(verification_role)  # type: ignore
        self.mod_roles = [self.guild.get_role(int(x)) for x in mod_roles.split()]  # type: ignore
        self.admin_roles = [self.guild.get_role(int(x)) for x in admin_roles.split()]  # type: ignore


@dataclass
class Guild:
    rowid: int
    guild: discord.Guild
    owner: discord.User
    blacklisted: bool

    def __init__(
        self,
        bot: commands.Bot,
        rowid: int,
        discord_id: int,
        owner_id: int,
        blacklisted: bool = False,
    ):
        self.rowid = rowid
        self.guild = bot.get_guild(discord_id)  # type: ignore
        self.owner = bot.get_user(owner_id)  # type: ignore
        self.blacklisted = blacklisted

        if self.guild is None:
            raise ValueError("Guild is not found")
        if self.owner is None:
            raise ValueError("Owner is not found")
