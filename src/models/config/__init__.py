import json
from enum import Enum
from typing import Any, Union, Dict, overload

from models import dataclasses


class Configs(Enum):
    """Перечисление конфигурационных файлов.

    Сопоставляет имя конфига с путём к файлу и классом-моделью.

    Используется для загрузки и десериализации конфигов.

    Пример:

    .. code-block:: python

        config = load_config(Configs.bot_info)

    """
    bot_info = "models/config/bot_info.json", dataclasses.BotInfo
    database = "models/config/database.json", dataclasses.Database


@overload
def load_config(file: str) -> Dict[str, Any]:
    ...

@overload
def load_config(file: Configs) -> dataclasses.BotInfo | dataclasses.Database:
    ...

def load_config(
    file: Union[Configs, str]
) -> Dict[str, Any] | dataclasses.BotInfo | dataclasses.Database:
    """Loads a config from a file into the model object.

    :param file: File path or element of the Configs enumeration
    :type file: Union[Configs, str]

    :return: Dictionary or configs model object
    :rtype: Dict[Any, Any] | dataclasses.BotInfo | dataclasses.Database
    """
    if isinstance(file, str):
        return json.load(open(file, "r"))
    else:
        return file.value[1](**json.load(open(file.value[0], "r")))
