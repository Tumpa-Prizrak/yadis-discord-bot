import sqlite3
from asyncio import run
from typing import Any, List, Self, Tuple
import os

from api.database.enums import DBFormat
from models.dataclasses import Database
from models.config import load_config, Configs

config = load_config(Configs.database)


class ConnectionClosed(Exception):
    """Exception thrown when trying to use a closed database connection.
    
    Inherited from Exception.
    """
    ...



class DatabaseWraper:
    """A wrapper for working with SQLite database.

    Allows you to open and close a connection, 
    execute database queries.

    Uses context manager to automatically 
    open and close a connection.

    Example usage:

    .. code-block:: python

        With DatabaseWraper('db.db') as db:
            db.execute('SELECT * FROM table').

    """
    def __init__(self, /, database_name: str) -> None:
        """Initialisation of the wrapper for the database.

        :param database_name: Database file name
        :type database_name: str
        """
        self.database_name: str = database_name
        self.cursor = None
        self.connection = None

    def __enter__(self) -> Self:
        """Opens a connection when used as a context manager."""
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore
        """Closes the connection when exiting the context manager.
     
        :param exc_type: Exception type
        :param exc_val: Exception value
        :param exc_tb: Exception stack trace
        """
        self.close()

    def open(self) -> None:
        """Opens a connection to the database."""
        if self._is_opened():
            return
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def close(self) -> None:
        """Closes the database connection"""
        if self._is_closed():
            return

        assert self.cursor is not None and self.connection is not None

        self.cursor = self.cursor.close()
        self.connection = self.connection.close()

    def execute(self, query: str, params: Tuple[Any]) -> List[Any]:
        """Executes an SQL query against a database.

        :param query: Query text 
        :type query: str

        :param params: Query parameters
        :type params: tuple

        :return: Query result
        :rtype: list
        """
        if self._is_closed():
            raise ConnectionClosed("Connection closed. You must use .open() first")

        assert self.cursor is not None

        return self.cursor.execute(query, params).fetchall()

    def _is_opened(self) -> bool:
        return not self._is_closed()

    def _is_closed(self) -> bool:
        return None in (self.connection, self.cursor)


class DatabaseConnection(DatabaseWraper):
    """A class for working with database connection.

    Inherits from DatabaseWrapper and adds methods
    for reading and writing data to the database.

    Example:

    .. code-block:: python

        With DatabaseConnection('data.db') as db:
            db.write("INSERT INTO table VALUES (?)", (1,))
            print(db.read("SELECT * FROM table", mode=DBFormat.List))

    """
    def __init__(self, /, database_name: str | None = None) -> None:
        """Initialisation of the database connection.

        :param database_name: Path to the database file, optional
        :type database_name: str
        """
        assert isinstance(config, Database)

        if database_name is None:
            database_name = config.database_path

        super().__init__(database_name)

    def read(self, query: str, *args: Any, mode: DBFormat) -> list[Any] | Any:
        """Executes a query to read data.

        :param query: SQL query text
        :type query: str

        :param args: Query parameters 
        :type args: list

        :param mode: Data formatting mode
        :type mode: DBFormat
        
        :return: Query result
        :rtype: list, dict or value
        """
        if self._is_closed():
            raise ConnectionClosed("Connection closed. You must use .open() first")
        return self._format_data(self.execute(query, args), mode)

    def write(
        self,
        query: str,
        *args: Any,
        log_errors: bool = True,
        raise_errors: bool = False,
    ) -> bool:
        """Executes a query to write data.

       :param query: SQL query text
       :type query: str
       
       :param args: Query parameters
       :type args: list

       :param log_errors: Log errors, default True
       :type log_errors: bool

       :param raise_errors: Raise errors, default False
       :type raise_errors: bool

       :return: Successful execution of the request 
       :rtype: bool
       """

        if self._is_closed():
            raise ConnectionClosed("Connection closed. You must use .open() first")

        assert self.connection is not None

        try:
            self.execute(query, args)
            self.connection.commit()
            return True
        except Exception as e:
            if log_errors:
                run(self.logger.error(e))  # type: ignore
            if raise_errors:
                raise e from e
            return False

    def _format_data(self, data: List[Any], mode: DBFormat) -> list[Any] | Any:
        match mode:
            case DBFormat.Raw:
                return data
            case DBFormat.One:
                try:
                    return data[0][0] if len(data) == 1 and len(data[0]) == 1 else data[0]
                except IndexError:
                    return None
            case DBFormat.List:
                try:
                    return [x[0] if len(x) == 1 else x for x in data]
                except IndexError:
                    return []


def GenerateDatabase() -> None:
    """Generates database by schema if it does not exist.

    Creates a database file using the path from the config if it does not exist.
    Executes the database schema script to initialise tables.

    Uses DatabaseWrapper to work with the database.
    """
    assert isinstance(config, Database)

    if os.path.exists(config.database_path):
        return

    with open(config.database_path, "rb") as f:
        if f.read() != b"":
            return

    with DatabaseWraper(config.database_path) as dbw, open(config.database_schema) as f:
        assert dbw.cursor is not None and dbw.connection is not None

        dbw.cursor.executescript(f.read())
        dbw.connection.commit()
