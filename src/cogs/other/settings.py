from src.models.bot import Yadis
from src.models.ui.view import settings
from discord.ext.commands import Cog
from discord import app_commands, Interaction

class SetupCog(Cog):
    def __init__(self, client: Yadis) -> None:
        self.client = client
    
    @app_commands.command(name="settings", description="Set up your server personally!")
    async def settings(self, interaction: Interaction):
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
