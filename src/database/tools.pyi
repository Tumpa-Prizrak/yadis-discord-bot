import sqlite3
from src.database.enums import DBFormat
from typing import Any, List, Self
from src.custom_logs import Logger
from asyncio import run
from src.models import error

class DatabaseConnection:
    """A class for connecting to and querying a SQLite database."""
    database_name: str
    cursor: sqlite3.Cursor | None
    connection: sqlite3.Connection | None
    logger: Logger

    def __init__(self, /, database_name: str = "src/database/database.db"):
        """Initialize the DatabaseConnection.
        
        Args:
            database_name (str, optional): The path to the database file. Defaults to "src/database/database.db".
        """
        ...

    def __enter__(self) -> Self: ...

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    
    def open(self) -> None:
        """Open the database connection."""
        ...

    def close(self) -> None:
        """Close the database connection."""
        ...

    def read(self, query: str, mode: DBFormat) -> List[Any] | Any:
        """Execute a query and return the results formatted based on the mode.
        
        Args:
            query (str): The SQL query to execute.
            mode (DBFormat): The format to return the results in.
            
        Returns:
            list | Any: The results of the query in the specified format.
            
        Raises:
            error.ConnetionClosed: If the connection is closed.
        """
        ...

    def write(self, query: str, log_errors: bool = True) -> bool:
        """Execute a write query on the database.
        
        Args:
            query (str): The SQL query to execute.
            log_errors (bool, optional): Whether to log any errors. Defaults to True.
            
        Returns:
            bool: True if the query executed successfully, False otherwise.
            
        Raises:
            error.ConnetionClosed: If the connection is closed.
        """
        ...

    def _execute(self, query: str) -> List[Any]:
        """Execute the given query.
        
        Summary: Execute a query on the database.
        
        Args:
            query (str): The SQL query to execute.
            
        Returns:
            list: The results of the query.
        """
        ...

    def _is_opened(self) -> bool:
        """Check if the database connection is open.
        
        Returns:
            bool: True if the connection is open, False otherwise.
        """
        ...

    def _is_closed(self) -> bool:
        """Check if the database connection is closed.
        
        Returns:
            bool: True if the connection is closed, False otherwise.
        """
        ...

    def _format_data(self, data: List[Any], mode: DBFormat) -> List[Any] | Any:
        """Format data from a query based on the specified mode.
        
        Args:
            data (list): The data returned from the query.
            mode (DBFormat): The format to return the data in.
            
        Returns:
            list | Any: The formatted data.
        """
        ...
