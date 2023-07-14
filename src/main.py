from bot.yadis import Yadis
from models.config import load_config, Configs
from models.dataclasses import BotInfo
from discord import Intents

bot_info: BotInfo = load_config(file=Configs.bot_info)  # type: ignore

bot = Yadis(
    command_prefix=bot_info.prefix,
    intents=Intents(bot_info.intents),
    token=bot_info.token,
)

bot.run()
