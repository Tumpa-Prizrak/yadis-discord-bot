from dataclasses import dataclass
from typing import List


@dataclass
class Database():
    database_path: str
    database_schema: str

@dataclass
class Logger():
    log_format: str
    dt_format: str
    filename_format: str

@dataclass
class BotInfo():
    token: str
    appid: int
    prefix: str
    debug_channel_id: int
    state_channel_id: int
    intents: int
    owners: List[int]
