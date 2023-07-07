import json
from enum import Enum
from typing import Any, Union, Dict

from src.config import pyconfig
from src.models import config


class Configs(Enum):
    """Enum representing the available config files."""

    bot_info = "src/config/bot_info.json", config.BotInfo
    logger = "src/config/logger.json", config.Logger
    database = "src/config/database.json", config.Database


def load_config(file: Union[Configs, str]) -> Dict[Any, Any] | config.BotInfo | config.Database | config.Logger:
    """Load a config file.

    Args:
        file (Configs | str): The config file to load. Either a Configs enum member or the file path.

    Returns:
        dict[str, Any]: The loaded config data.
    """
    if isinstance(file, str):
        return json.load(open(file, "r"))
    else:
        return file.value[1](**json.load(open(file.value[0], "r")))
