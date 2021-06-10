"""Test for task02 - Original info"""
from homework5.task02 import save_original_info


def double_decor(func):
    """Decorator for testing save_original_info decorator"""

    @save_original_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper"""
        return func

    return wrapper


def func_for_test():
    """Returns nothing"""
    pass


decorated_func = double_decor(func_for_test)


def test_decorator_name_doc_original_info():
    assert decorated_func.__doc__ == """Returns nothing"""
    assert decorated_func.__name__ == """func_for_test"""
    assert decorated_func.__original_func == func_for_test
    assert hasattr(decorated_func, "__original_func") and callable(
        getattr(decorated_func, "__original_func")
    )
