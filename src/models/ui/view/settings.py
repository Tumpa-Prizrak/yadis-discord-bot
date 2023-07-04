from typing import Any, Optional, Union
from discord import ui
from discord import Interaction
from discord.emoji import Emoji
from discord.enums import ButtonStyle
from discord.interactions import Interaction
from discord import Message
from discord.partial_emoji import PartialEmoji


class MainView(ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        pass

    async def on_timeout(self) -> None:
        pass


class TopLevelButton(ui.Button):
    def __init__(
        self,
        category: str,
        message: Message
    ):
        super().__init__(
            style=ButtonStyle.secondary,
            label=category,
            disabled=False,
            custom_id=None,
            url=None,
            emoji='📁',
            row=None,
        )
    
    async def callback(self, interaction: Interaction):
        pass
