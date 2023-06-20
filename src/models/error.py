from discord import errors
from discord.ext.commands import errors as commands_errors

class NotOfficial(Warning): ...

_all = [NotOfficial]
_warnings = [NotOfficial]
_errors = []
