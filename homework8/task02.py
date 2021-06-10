""""Task02 - TableData"""
import sqlite3
from functools import wraps
from typing import Callable, Iterator


class TableData:
    """Wrapper class for database table that works as collection object.
    Database should be in sqlite3 format and its tables must have column name
    with unique values."""

    def __init__(self, database_name: str, table_name: str) -> None:
        self.database_name = database_name
        self.table_name = table_name

    def _connection(func) -> Callable:
        """Decorator for connection to database and
        disconnection after working with the database"""

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            to_return = func(self, cursor, *args, **kwargs)
            conn.close()
            return to_return

        return wrapper

    @_connection
    def __getitem__(self, cursor, name: str) -> str:
        """Checks if the name of president exists in the table"""
        result = cursor.execute(
            "SELECT * FROM %s WHERE name='%s'" % (self.table_name, name)
        ).fetchone()
        if result:
            return "%s in %s" % (list(result)[0], self.table_name)
        return "This name is not in %s" % self.table_name

    @_connection
    def __iter__(self, cursor) -> Iterator:
        """Iteration method which allows to use table in "for"-loop"""
        cursor.row_factory = self._dict_factory
        rows = cursor.execute("SELECT * FROM %s" % self.table_name).fetchall()
        return iter(rows)

    @staticmethod
    def _dict_factory(cursor, row):
        """Gives names of columns"""
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    @_connection
    def __len__(self, cursor) -> int:
        """Returns current amount of rows in the table"""
        row_amount = cursor.execute(
            "SELECT COUNT(*) FROM %s" % self.table_name
        ).fetchone()[0]
        return row_amount
