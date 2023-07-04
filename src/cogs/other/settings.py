import discord
from discord.ext import commands
from src.models.bot import Yadis
from src.models.ui.view import settings

class SetupCog(commands.Cog):
    def __init__(self, client: Yadis) -> None:
        self.client = client
    
    @discord.app_commands.command(name="settings", description="Set up your server personally!")
    async def settings(self, interaction: discord.Interaction):
        """
            Embed (With buttons | dropdown):
                - Category1:
                    - command1.1:
                        - modal
                    - command1.2:
                        - modal
                    ...
                - Category2:
                    - command2.1:
                        - modal
                    - command2.2:
                        - modal
                    ...
                ...
        """
        pass


async def setup(bot: Yadis):
    await bot.add_cog(SetupCog(bot))
