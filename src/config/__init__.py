from enum import Enum
import json
from typing import Any
from src.config import pyconfig


class Configs(Enum):
    bot_info = "src/config/bot_info.json"
    logger = "src/config/logger.json"


def load_config(file: Configs | str) -> dict[str, Any]:
    return json.load(open(file if isinstance(file, str) else file.value, "r"))
