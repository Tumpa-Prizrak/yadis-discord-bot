from dataclasses import dataclass
import discord
import typing
from discord.ext import commands
# from enum import StrEnum, auto


@dataclass
class Database:  # Config only
    """Database Configuration Class.

    Attributes:

    - database_path: The path to the database file 
    - database_schema: Path to the database schema
    """
    database_path: str
    database_schema: str
    

@dataclass
class BotInfo:  # Config only
    """Bot Configuration Class.

    Attributes:

    - token: The token of the bot
    - prefix: Command prefix 
    - intents: Bot's intentions
    """
    token: str
    prefix: str
    intents: int
    devs: list[int]


@dataclass
class Settings:  # Database only
    """Server Settings Class.

    Attributes:

    - rowid: ID of the record in the database
    - guild: Server object
    - blacklisted: Blacklist
    - custom_voice_entery: Login channel
    - welcome_channel: Welcome channel
    - welcome_messages: Welcome messages
    - verification_role: Verification role 
    - mod_roles: Moderator Roles
    - admin_roles: Admin roles
    """
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
    """Server model class.

    Attributes:

    - rowid: The ID of the record in the database
    - guild: Server object
    - owner: Server owner
    - blacklisted: Blacklisted
    """
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


@dataclass
class Error:
    title: str
    description: str
    code: int


