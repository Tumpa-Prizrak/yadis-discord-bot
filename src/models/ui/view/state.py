import discord
from src.models.ui import modal


class StateView(discord.ui.View):
    @discord.ui.button(label="Check", emoji="✅")
    async def check(self, interaction: discord.Interaction, _):
        await interaction.response.send_modal(modal.state.OnlineModal())  # type: ignore
