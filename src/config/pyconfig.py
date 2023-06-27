import colorama
import discord
from dataclasses import dataclass


@dataclass
class Version:
    """Represents a software version."""
    
    major: int
    """The major version number."""
    
    middle: int
    """The middle version number."""
    
    minor: int
    """The minor version number."""
    
    official: bool
    """Whether this is an official release."""
    
    final: bool
    """Whether this is a final release."""


class Colors:
    """Color constants."""
    
    dt_color = colorama.Fore.BLUE
    """The color for timestamps."""
    
    source_color = colorama.Fore.MAGENTA
    """The color for log message sources."""
    
    reset = colorama.Fore.RESET
    """The color reset code."""


def to_dscolor(color: colorama.Fore):
    """Convert a colorama Fore color to a discord.Color.
    
    Args:
        color (colorama.Fore): The colorama Fore color to convert.
        
    Returns:
        discord.Color: The equivalent discord.Color.
    """
    return color_map.get(color, discord.Color.green())


color_map = {
    colorama.Fore.RED: discord.Color.red(),
    colorama.Fore.GREEN: discord.Color.green(),
    colorama.Fore.YELLOW: discord.Color.gold(),
    colorama.Fore.BLUE: discord.Color.blue(),
    colorama.Fore.MAGENTA: discord.Color.purple(),
    colorama.Fore.CYAN: discord.Color.teal(),
    colorama.Fore.WHITE: discord.Color.from_rgb(255, 255, 255),
    colorama.Fore.BLACK: discord.Color.from_rgb(0, 0, 0), 
}

verson = Version(0, 0, 1, False, False)
