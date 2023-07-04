from dataclasses import dataclass

import colorama
from discord import Color


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


def to_dscolor(color: colorama.Fore):  # type: ignore
    """Convert a colorama Fore color to a Color.

    Args:
        color (colorama.Fore): The colorama Fore color to convert.

    Returns:
        Color: The equivalent Color.
    """
    return color_map.get(color, Color.green())


color_map = {
    colorama.Fore.RED: Color.red(),
    colorama.Fore.GREEN: Color.green(),
    colorama.Fore.YELLOW: Color.gold(),
    colorama.Fore.BLUE: Color.blue(),
    colorama.Fore.MAGENTA: Color.purple(),
    colorama.Fore.CYAN: Color.teal(),
    colorama.Fore.WHITE: Color.from_rgb(255, 255, 255),
    colorama.Fore.BLACK: Color.from_rgb(0, 0, 0),
}

verson = Version(0, 0, 1, True, False)
