from enum import Enum, auto


class DBFormat(Enum):
    """The format to return data from the database in.

    Raw - Return the row data
    List - Return the data as a list
    One - Return a single value
    """

    Raw = auto()
    List = auto()
    One = auto()
