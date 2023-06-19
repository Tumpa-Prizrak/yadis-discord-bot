from discord.ext import commands
import discord
from src.config import pyconfig
from src import config
from src import custom_logs

class Cog(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.clinet = client
        self.logger = custom_logs.Logger("State", client)
        self.bot_config = config.load_config(config.Configs.bot_info)

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            channel = self.clinet.get_channel(self.bot_config['state_channel_id'])
            await channel.purge()
            await channel.send(view=self.StateView(timeout=None), content="Press button to check bot state. If bot is offline you'll get interaction error")
        except KeyError:
            self.logger.error("Key 'state_channel_id' is not found at bot_info")

    class StateView(discord.ui.View):
        @discord.ui.Button(style=discord.ui.ButtonStyle.green, label="Check", emoji="✅") # FIXME module 'discord.ui' has no attribute 'ButtonStyle'
        async def check(self, _, interaction: discord.Interaction):
            await interaction.response.send_modal(discord.ui.Modal(title="Bot is online"))

async def setup(bot: commands.Bot):
    if pyconfig.verson.official:
        await bot.add_cog(Cog(bot))
    else:
        raise ValueError("Don't run cause it's not an official bot. It's not an error, keep going")
