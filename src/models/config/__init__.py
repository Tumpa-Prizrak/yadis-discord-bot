import json
from enum import Enum
from typing import Any, Union, Dict

from models import dataclasses


class Configs(Enum):
    """Enum representing the available config files."""

    bot_info = "models/config/bot_info.json", dataclasses.BotInfo
    database = "models/config/database.json", dataclasses.Database


def load_config(
    file: Union[Configs, str]
) -> Dict[Any, Any] | dataclasses.BotInfo | dataclasses.Database:
    """Load a config file.

    ### Args:
        file (Configs | str): The config file to load. Either a Configs enum member or the file path.

    ### Returns:
        dict[str, Any]: The loaded config data.
    """
    if isinstance(file, str):
        return json.load(open(file, "r"))
    else:
        return file.value[1](**json.load(open(file.value[0], "r")))
