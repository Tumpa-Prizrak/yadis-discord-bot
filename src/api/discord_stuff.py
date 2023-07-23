import discord
from models import config
from models.dataclasses import BotInfo

bot_data: BotInfo = config.load_config(config.Configs.bot_info)  # type: ignore

def check_dev(user: discord.User):
    return user.id in bot_data.devs
