import sqlite3
from .enums import State

class DatabaseConnection:
    def __init__(self, /, database_name: str = "src/database/database.db"):
        self.database_name = database_name if database_name.startswith("src/") else "src/database/" + database_name
        self.cursor = None
        self.connection = None
    
    def open(self):
        if self._is_opened(): return
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def close(self):
        if self._is_closed(): return
        self.cursor.close()
        self.connection.close()
        self.cursor = None
        self.connection = None

    def read(self, query: str, mode: State):
        pass

    def write(self):
        pass

    def _execute(self):
        pass

    def _is_opened(self):
        return self.connection is not None and self.cursor is not None

    def _is_closed(self):
        return self.connection is None and self.cursor is None
