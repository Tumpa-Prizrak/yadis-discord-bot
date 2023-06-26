from src.models.bot import Yadis
from src import config
from src import custom_logs
from asyncio import run
from discord.ext.commands import when_mentioned_or


bot_info = config.load_config(config.Configs.bot_info)

log = custom_logs.Logger("Main")
run(log.info(message="Loading...", to_channel=False, to_file=False))

bot = Yadis(
    token=bot_info.get("token"),
    command_prefix=when_mentioned_or(bot_info.get("prefix")),
    owner_id=bot_info.get("owner"),
    debug_channel_id=bot_info.get("debug_channel_id"), # type: ignore
    intents=bot_info.get("intents"), # type: ignore
)

bot.run()
