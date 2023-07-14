from dataclasses import dataclass


@dataclass
class Database:
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
class BotInfo:
    token: str
    prefix: str
    intents: int
