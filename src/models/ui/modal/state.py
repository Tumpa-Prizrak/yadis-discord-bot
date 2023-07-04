from discord import ui
from discord import TextStyle
from discord import Interaction


class OnlineModal(ui.Modal, title="Bot is online~"):
    """A modal displayed when the check if bot's online."""

    answer = ui.TextInput(label="How are you?", style=TextStyle.paragraph)

    async def on_submit(self, interaction: Interaction):
        await interaction.response.send_message(
            content="Have a nice day!", ephemeral=True
        )
