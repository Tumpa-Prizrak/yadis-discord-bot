from os import listdir
from discord.ext.commands import Bot  # type: ignore
import traceback


async def load_extensions(bot: Bot, extensions_dir: str, extension_prefix: str) -> None:
    """
    Загружает модули из указанной директории.
    
    Параметры:
    - bot: Yadis - бот
    - extensions_dir: str - директория с модулями
    - extension_prefix: str - префикс имени модуля
    - load_path: str - путь для импорта модуля
    
    Загружает модули, имена которых начинаются с extension_prefix и 
    заканчиваются на .py из директории extensions_dir, импортируя 
    их относительно load_path.
    """
    load_path = extensions_dir.replace("/", ".")

    for extension in listdir(extensions_dir):
        if extension.endswith(".py") and extension.startswith(extension_prefix):
            try:
                await bot.load_extension(f"{load_path}.{extension[:-3]}")
                bot.logger.info(f"{extension[len(extension_prefix):-3]} loaded")  # type: ignore
            except Exception:
                bot.logger.error(f"Extension {load_path}.{extension[len(extension_prefix):-3]} raised following error:\n{traceback.format_exc()}\n\n")  # type: ignore
