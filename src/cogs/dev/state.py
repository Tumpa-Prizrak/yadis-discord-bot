import time

from discord import TextChannel
from discord.ext import commands

from src import config, custom_logs
from src.config import pyconfig
from src.models import error
from src.models.ui import view


class Cog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.logger = custom_logs.Logger("State", client)
        self.bot_config = config.load_config(config.Configs.bot_info)
        self.dt_format = config.load_config(config.Configs.logger).get("dt_format")

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            channel: TextChannel = self.client.get_channel(self.bot_config["state_channel_id"])  # type: ignore
            await channel.purge()
            await channel.send(
                view=view.state.StateView(timeout=None),
                content="**Eng:** Press button to check bot state. If bot is offline you'll get interaction error\n"
                "**Rus:** Нажмите кнопку, чтобы проверить состояние бота. Если бот не в сети, вы получите ошибку взаимодействия",
            )
            now = round(time.time())
            await channel.send(
                content=f"**Eng: Bot started at <t:{now}>(<t:{now}:R>)\nRus: Бот запущен в <t:{now}>(<t:{now}:R>)**"
            )
        except KeyError:
            await self.logger.error("Key 'state_channel_id' is not found at bot_info")


async def setup(bot: commands.Bot):
    if pyconfig.verson.official:
        await bot.add_cog(Cog(bot))
    else:
        raise error.NotOfficial(
            "Don't run cause it's not an official bot. It's not an error, keep going"
        )
