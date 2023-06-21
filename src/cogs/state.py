from discord.ext import commands
import discord
from src.config import pyconfig
from src import config
from src import custom_logs
from src.models import error


class Cog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.clinet = client
        self.logger = custom_logs.Logger("State", client)
        self.bot_config = config.load_config(config.Configs.bot_info)

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            channel = self.clinet.get_channel(self.bot_config["state_channel_id"])
            await channel.purge()
            await channel.send(
                view=self.StateView(timeout=None),
                content="**Eng:** Press button to check bot state. If bot is offline you'll get interaction error\n**Rus:** Нажмите кнопку, чтобы проверить состояние бота. Если бот не в сети, вы получите ошибку взаимодействия",
            )
        except KeyError:
            self.logger.error("Key 'state_channel_id' is not found at bot_info")


async def setup(bot: commands.Bot):
    if pyconfig.verson.official:
        await bot.add_cog(Cog(bot))
    else:
        raise error.NotOfficial(
            "Don't run cause it's not an official bot. It's not an error, keep going"
        )
