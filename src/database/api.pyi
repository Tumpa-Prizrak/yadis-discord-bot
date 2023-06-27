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
) -> discordModels.Guild:
    """Get a Guild object.
    
    Args:
        bot (Yadis): The bot object.
        owner (Optional[discord.User | int]): The guild owner object or ID.
        guild (Optional[int | discord.Guild]): The guild object or ID.
        
    Returns:
        discordModels.Guild: The Guild object.
    """
    ...

async def _resolve_user(bot, user_id) -> discord.User:
    """Resolve a user ID to a User object.
    
    Args:
        bot (Yadis): The bot object.
        user_id (discord.User | int): The user ID or User object.
        
    Returns:
        discord.User: The User object.
    """
    ...

async def _get_guild_by_owner(bot, owner) -> discord.Guild:
    """Get a guild by its owner.
    
    Args:
        bot (Yadis): The bot object.
        owner (discord.User): The guild owner.
        
    Returns:
        discord.Guild: The guild object.
    """
    ...  

async def _resolve_guild(bot, guild_id) -> discord.Guild:
    """Resolve a guild ID to a Guild object.
    
    Args:
        bot (Yadis): The bot object.
        guild_id (int | discord.Guild): The guild ID or Guild object.
        
    Returns:
        discord.Guild: The Guild object.
    """
    ...

async def _get_voice_channel(bot, guild) -> Optional[discord.VoiceChannel]:
    """Get the voice channel for a guild.
    
    Args:
        bot (Yadis): The bot object.
        guild (discord.Guild): The guild object.
        
    Returns:
        Optional[discord.VoiceChannel]: The voice channel or None if not found.
    """
    ...
