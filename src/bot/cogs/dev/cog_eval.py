from discord.ext import commands
import discord
from enum import StrEnum, auto


class eval_mode(StrEnum):
    python = auto()
    shell = auto()
    sql = auto()


class EvalCog(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        super().__init__()
        self.client: commands.Bot = client
    
    @discord.app_commands.command()
    async def eval(self, interaction: discord.Interaction, mode: eval_mode):
        await interaction.response.send_message(mode.value)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EvalCog(bot))
