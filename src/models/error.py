from discord import errors
from discord.ext.commands import errors as commands_errors


class NotOfficial(Warning):
    """A warning raised when an unofficial Bot is used."""
    ...

class ConnectionClosed(Exception):
    """An exception raised when trying to perform an operation on a closed database connection."""
    ...

    
_all = [NotOfficial, ConnetionClosed]
_warnings = [NotOfficial]
_errors = [ConnetionClosed
