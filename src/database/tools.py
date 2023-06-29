import sqlite3
from src.database.enums import DBFormat
from typing import Any
from src.custom_logs import Logger
from asyncio import run
from src.models import error


class DatabaseConnection:
    def __init__(self, /, database_name: str = "src/database/database.db"):
        self.database_name = (
            database_name if "/" in database_name else f"src/database/{database_name}"
        )
        self.cursor = None
        self.connection = None
        self.logger = Logger("DatabaseConnection")

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

    def read(self, query: str, *args, mode: DBFormat) -> list | Any:
        if self._is_closed():
            raise error.ConnectionClosed(
                "Connection closed. You must use .open() first"
            )
        return self._format_data(self._execute(query, args), mode)

    def write(
        self, query: str, *args, log_errors: bool = True, raise_errors: bool = False
    ) -> bool:
        if self._is_closed():
            raise error.ConnectionClosed(
                "Connection closed. You must use .open() first"
            )

        assert self.connection is not None

        try:
            self._execute(query, args)
            self.connection.commit()
            return True
        except Exception as e:
            if raise_errors:
                raise e from e
            elif log_errors:
                run(self.logger.error(e))
            return False

    def _execute(self, query: str, params: tuple) -> list:
        assert self.cursor is not None

        return self.cursor.execute(query, params).fetchall()

    def _is_opened(self):
        return not self._is_closed()

    def _is_closed(self):
        return self.connection is None or self.cursor is None

    def _format_data(self, data, mode: DBFormat) -> list | Any:
        if mode == DBFormat.Raw or not data:
            return data
        elif mode == DBFormat.List:
            return [x[0] if len(x) == 1 else x for x in data]
        elif mode == DBFormat.One:
            return data[0][0] if len(data) == 1 and len(data[0]) == 1 else data[0]
