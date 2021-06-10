""""Task01 - KeyValueStorage"""
from typing import Any


class KeyValueStorage:
    """Wrapper class that works as key-value storage.
    It takes a file with lines like key=value and it behaves with lines like a dictionary.
    There is an access to keys and values as collection items: storage[key] == value
    Also, there is an access to keys and values as attributes: storage.key == value"""

    def __init__(self, file_path: str):
        with open(file_path) as fi:
            for line in fi.readlines():
                key, value = line.strip().split("=")
                if not key.isidentifier():
                    raise ValueError
                value = int(value) if value.isdigit() else value
                self.__dict__[key] = value

    def __getitem__(self, key: str) -> Any:
        """Implements access to a value as a collection item."""
        return self.__dict__[key]
