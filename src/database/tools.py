import sqlite3
from asyncio import run
from typing import Any, Union
import os

from src.custom_logs import Logger
from src.database.enums import DBFormat
from src.models import error
from src.models.config import Database
from src.config import load_config, Configs

config = load_config(Configs.database)


class DatabaseWraper:
    def __init__(self, /, database_name: str) -> None:
        self.database_name = database_name
        self.cursor = None
        self.connection = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def open(self):
        if self._is_opened():
            return
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def close(self):
        if self._is_closed():
            return

        assert self.cursor is not None
        assert self.connection is not None

        self.cursor = self.cursor.close()
        self.connection = self.connection.close()

    def execute(self, query: str, params: tuple) -> list:
        assert self.cursor is not None

        return self.cursor.execute(query, params).fetchall()

    def _is_opened(self):
        return not self._is_closed()

    def _is_closed(self):
        return self.connection is None or self.cursor is None


class DatabaseConnection(DatabaseWraper):
    def __init__(self, /, database_name: str = None):  # type: ignore
        assert isinstance(config, Database)

        if database_name is None:
            database_name = config.database_path
        super().__init__(database_name)
        self.logger = Logger("DatabaseConnection")

    def read(self, query: str, *args, mode: DBFormat) -> Union[list, Any]:
        if self._is_closed():
            raise error.ConnectionClosed(
                "Connection closed. You must use .open() first"
            )
        return self._format_data(self.execute(query, args), mode)

    def write(
        self, query: str, *args, log_errors: bool = True, raise_errors: bool = False
    ) -> bool:
        if self._is_closed():
            raise error.ConnectionClosed(
                "Connection closed. You must use .open() first"
            )

        assert self.connection is not None

        try:
            self.execute(query, args)
            self.connection.commit()
            return True
        except Exception as e:
            if raise_errors:
                raise e from e
            elif log_errors:
                run(self.logger.error(e))  # type: ignore
            return False

    def _format_data(self, data, mode: DBFormat) -> Union[list, Any]:
        if mode == DBFormat.Raw or not data:
            return data
        elif mode == DBFormat.List:
            return [x[0] if len(x) == 1 else x for x in data]
        elif mode == DBFormat.One:
            return data[0][0] if len(data) == 1 and len(data[0]) == 1 else data[0]


def GenerateDatabase():
    assert isinstance(config, Database)

    if os.path.exists(config.database_path):
        return

    with open(config.database_path, "rb") as f:
        if f.read() != b"":
            return

    with DatabaseWraper(config.database_path) as dbw, open(config.database_schema) as f:
        assert dbw.cursor is not None
        assert dbw.connection is not None

        dbw.cursor.executescript(f.read())
        dbw.connection.commit()
