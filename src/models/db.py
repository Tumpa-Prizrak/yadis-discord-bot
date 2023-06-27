from dataclasses import dataclass
from typing import Optional

@dataclass
class Guild:
    rowid: int
    guild_id: int
    name: str
    owner: int
    custom_voice_entery_id: Optional[int]
    member_count: int
