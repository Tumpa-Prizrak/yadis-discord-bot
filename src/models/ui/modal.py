import discord

class OnlineModal(discord.ui.Modal, title='Bot is online~'):
    answer = discord.ui.TextInput(label='How are you?', style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="Have a nice day!", ephemeral=True)
