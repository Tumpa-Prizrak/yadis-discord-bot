from discord import ui
from discord import Interaction
from src.models.ui import modal


class StateView(ui.View):
    @ui.button(label="Check", emoji="✅")
    async def check(self, interaction: Interaction, button):
        await interaction.response.send_modal(modal.state.OnlineModal())  # type: ignore
