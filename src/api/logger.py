import logging
from logging.handlers import RotatingFileHandler


class LevelFilter(logging.Filter):
   """Filter log entries by level.

   :param level: Maximum level of records to output
   :type level: int

   Outputs only records with a level lower than the level specified at initialisation.

   Example:

   .. code-block:: python

       f = LevelFilter(logging.WARNING)
       logger.addFilter(f)

   This will only output records with levels DEBUG, INFO, 
   but not WARNING, ERROR or CRITICAL.
   """
   def __init__(self, level):  # type: ignore
       """Initialises the filter with the specified level
       
       :param level: Maximum level of records to output
       :type level: int
       """
       self.level = level

   def filter(self, record) -> bool:  # type: ignore
       """Filters the record by level
       
       :param record: Record to filter
       :type record: LogRecord
       
       :return: True if the record level is below the specified level
       :rtype: bool
       """
       return record.levelno < self.level


def setup_logger() -> logging.Logger:
    """Configures and returns the application logger.

    Creates a logger, adds two handlers (for writing to files)
    and configures a formatter for the records.

    :return: Configured logger
    :rtype: logging.Logger
    """
    logger: logging.Logger = logging.getLogger("discord")
    logger.addHandler(get_file_handler())
    logger.addHandler(get_error_handler())

    return logger


def get_file_handler() -> RotatingFileHandler:
    """Returns a handler for writing general logs to a file.

    :return: Handler for info level in shared logs
    :rtype: RotatingFileHandler
    """
    file_handler = RotatingFileHandler(
        filename="../logs/discord.log",
        encoding="utf-8",
        maxBytes=32 * 1024 * 1024,
        backupCount=10,
    )
    file_handler.setFormatter(get_file_formatter())
    file_handler.setLevel(logging.INFO)
    file_handler.addFilter(LevelFilter(logging.ERROR))

    return file_handler

def get_error_handler() -> RotatingFileHandler:
    """Returns a handler for writing errors to a separate file.

    :return: Handler for error level 
    :rtype: RotatingFileHandler
    """
    file_handler = RotatingFileHandler(
        filename="../logs/error.log",
        encoding="utf-8",
        maxBytes=32 * 1024 * 1024,
        backupCount=10,
    )
    file_handler.setFormatter(get_file_formatter())
    file_handler.setLevel(logging.ERROR)

    return file_handler


def get_file_formatter() -> logging.Formatter:
    """Returns a formatter for file handlers.
    
    :return: Formatter for ``{`` style logging. 
    :rtype: logging.Formatter
    """
    dt_fmt = "%Y-%m-%d %H:%M:%S"
    return logging.Formatter(
        "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
    )
