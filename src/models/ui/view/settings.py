from discord import ui
from discord import Interaction

class MainView(ui.View):
    @ui.button()
    async def button(self, button: ui.Button, interaction: Interaction):
        await interaction.response.send_message("Button Clicked!")
