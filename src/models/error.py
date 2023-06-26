from discord import errors
from discord.ext.commands import errors as commands_errors


class NotOfficial(Warning):
    ...

class ConnetionClosed(Exception):
    ...


_all = [NotOfficial, ConnetionClosed]
_warnings = [NotOfficial]
_errors = [ConnetionClosed]
