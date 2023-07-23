from discord.ext import commands


class InfoCog(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        super().__init__()
        self.client = client


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(InfoCog(bot))
