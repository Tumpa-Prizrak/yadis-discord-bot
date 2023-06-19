from src.models.bot import Yadis
from src import config
from src import custom_logs
from asyncio import run

bot_info = config.load_config(config.Configs.bot_info)

log = custom_logs.Logger("Main")
run(log.info(message="Loading...", to_channel=False, to_file=False))

bot = Yadis(
    token=bot_info.get("token"),
    command_prefix=bot_info.get("prefix"),
    owner_id=bot_info.get("owner"),
    debug_channel_id=bot_info.get("debug_channel_id"),
    intents=bot_info.get("intents"),
)

bot.run()
