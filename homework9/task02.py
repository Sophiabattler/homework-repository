"""Task02 - Suppressor"""
from contextlib import contextmanager
from typing import ContextManager


class MySuppressor:
    """Context manager that suppresses passed exception"""

    def __init__(self, error: Exception):
        self.error = error

    def __enter__(self):
        """Enter the runtime context"""
        return self

    def __exit__(self, exp_type: type, exp_value: type, traceback: type) -> bool:
        """Exits the runtime context and return a Boolean flag
        indicating if any exception that occurred should be suppressed.
        Here the flag is True which means that exceptions will be suppressed"""
        print(type(traceback))
        return exp_type is not None and issubclass(exp_type, self.error)


@contextmanager
def my_suppressor(my_error: Exception) -> ContextManager:
    """Generator which suppresses passed exception"""
    try:
        yield
    except my_error:
        pass
