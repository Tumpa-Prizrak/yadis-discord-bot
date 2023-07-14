from logging import getLogger, Logger, StreamHandler, INFO, DEBUG, Formatter
from logging.handlers import RotatingFileHandler
from typing import TextIO


def setup_logger() -> Logger:
    logger: Logger = getLogger("discord")

    file_handler: RotatingFileHandler = get_file_handler()
    console_handler: StreamHandler[TextIO] = get_console_handler()
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def get_file_handler() -> RotatingFileHandler:
    file_handler = RotatingFileHandler(
        filename="..\\logs\\discord.log",
        encoding="utf-8",
        maxBytes=32 * 1024 * 1024,
        backupCount=10,
    )
    file_handler.setFormatter(get_file_formatter())
    file_handler.setLevel(INFO)

    return file_handler


def get_console_handler() -> StreamHandler[TextIO]:
    console_handler = StreamHandler()
    console_handler.setFormatter(get_console_formatter())
    console_handler.setLevel(DEBUG)

    return console_handler


def get_file_formatter() -> Formatter:
    dt_fmt = "%Y-%m-%d %H:%M:%S"
    return Formatter(
        "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
    )


def get_console_formatter() -> Formatter:
    return Formatter("{message}", style="{")
