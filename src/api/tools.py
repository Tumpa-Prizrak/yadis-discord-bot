from os import listdir
from discord.ext.commands import Bot  # type: ignore
import traceback


async def load_extensions(bot: Bot, extensions_dir: str, extension_prefix: str) -> None:
    """
    Loads modules from the specified directory.
    
    Parameters:
    - bot: Yadis - bot
    - extensions_dir: str - directory with modules
    - extension_prefix: str - module name prefix
    - load_path: str - path to import the module.
    
    Loads modules, whose names start with extension_prefix and 
    .py from the extensions_dir directory, importing them relative to load_path. 
    them relative to load_path.
    """
    load_path = extensions_dir.replace("/", ".")

    for extension in listdir(extensions_dir):
        if extension.endswith(".py") and extension.startswith(extension_prefix):
            try:
                await bot.load_extension(f"{load_path}.{extension[:-3]}")
                bot.logger.info(f"{extension[len(extension_prefix):-3]} loaded")  # type: ignore
            except Exception:
                bot.logger.error(f"Extension {load_path}.{extension[len(extension_prefix):-3]} raised following error:\n{traceback.format_exc()}\n\n")  # type: ignore
