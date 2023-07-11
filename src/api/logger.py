import logging
import logging.handlers


def setup_logger():
    logger = logging.getLogger("discord")

    file_handler = get_file_handler()
    console_handler = get_console_handler()
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def get_file_handler():
    file_handler = logging.handlers.RotatingFileHandler(
        filename="..\\logs\\discord.log",
        encoding="utf-8",
        maxBytes=32 * 1024 * 1024,
        backupCount=10,
    )
    file_handler.setFormatter(get_file_formatter())
    file_handler.setLevel(logging.INFO)

    return file_handler


def get_console_handler():
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(get_console_formatter())
    console_handler.setLevel(logging.DEBUG)

    return console_handler


def get_file_formatter():
    dt_fmt = "%Y-%m-%d %H:%M:%S"
    return logging.Formatter(
        "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
    )


def get_console_formatter():
    return logging.Formatter("{message}", style="{")
