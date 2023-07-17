import sqlite3
from asyncio import run
from typing import Any, List, Self, Tuple
import os

from api.database.enums import DBFormat
from models.dataclasses import Database
from models.config import load_config, Configs
from models.error import ConnectionClosed

config = load_config(Configs.database)


class DatabaseWraper:
    def __init__(self, /, database_name: str) -> None:
        self.database_name: str = database_name
        self.cursor = None
        self.connection = None

    def __enter__(self) -> Self:
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # type: ignore
        self.close()

    def open(self) -> None:
        if self._is_opened():
            return
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def close(self) -> None:
        if self._is_closed():
            return

        assert self.cursor is not None and self.connection is not None

        self.cursor = self.cursor.close()
        self.connection = self.connection.close()

    def execute(self, query: str, params: Tuple[Any]) -> List[Any]:
        if self._is_closed():
            raise ConnectionClosed("Connection closed. You must use .open() first")

        assert self.cursor is not None

        return self.cursor.execute(query, params).fetchall()

    def _is_opened(self) -> bool:
        return not self._is_closed()

    def _is_closed(self) -> bool:
        return None in (self.connection, self.cursor)


class DatabaseConnection(DatabaseWraper):
    def __init__(self, /, database_name: str | None = None) -> None:
        assert isinstance(config, Database)

        if database_name is None:
            database_name = config.database_path

        super().__init__(database_name)

    def read(self, query: str, *args: Any, mode: DBFormat) -> list[Any] | Any:
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


def GenerateDatabase():
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
