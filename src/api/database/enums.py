from enum import Enum, auto


class DBFormat(Enum):
   """Listing of database data formatting modes.

    Allows you to specify the required mode when making queries to the database.

    Mode options:

    - Raw - Returns the data as is
    - List - Returns a list of values
    - One - Returns a single value

    Example:

    .. code-block:: python
        
        data = db.read("SELECT * FROM table", mode=DBFormat.List)
   """
   Raw = auto()
   List = auto() 
   One = auto()

