from os import listdir
from typing import overload
from discord.ext.commands import Bot  # type: ignore
import traceback
import discord


async def load_extensions(bot: Bot, extensions_dir: str, extension_prefix: str) -> None:
    """Loads all extensions from the specified directory into the bot.

   :param bot: Bot instance for loading extensions
   :type bot: Bot

   :param extensions_dir: Path to the directory with extensions
   :type extensions_dir: str

   :param extension_prefix: Extensions file name prefix
   :type extension_prefix: str

   For each extension file in the directory, the following is performed:

   1. Loading the extension module
   2. Call bot.load_extension() to load it
   3. Logging the result

   Allows to load all extensions from the directory.
   """
    load_path = extensions_dir.replace("/", ".")

    for extension in listdir(extensions_dir):
        if extension.endswith(".py") and extension.startswith(extension_prefix):
            try:
                await bot.load_extension(f"{load_path}.{extension[:-3]}")
                bot.logger.info(f"{extension[len(extension_prefix):-3]} loaded")  # type: ignore
            except Exception:
                bot.logger.error(f"Extension {load_path}.{extension[len(extension_prefix):-3]} raised following error:\n{traceback.format_exc()}\n\n")  # type: ignore


def generate_error_embed(obj, /) -> discord.Embed:
    return discord.Embed(title=title, description=description, color=discord.Color.red()).set_image(url=f"https://http.cat/{code}.jpg")
