import discord
from src.models.ui import modal

class StateView(discord.ui.View):
        @discord.ui.button(
            label="Check", emoji="✅"
        )  # FIXME module 'discord.ui' has no attribute 'ButtonStyle'
        async def check(self, interaction: discord.Interaction, _):
            await interaction.response.send_modal(modal.OnlineModal())
