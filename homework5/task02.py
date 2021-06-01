"""Task02 - Original info"""
import functools


def save_original_info(func):
    """Function-wrapper for  wrapper which saves information about original function
    and add attribute with link to original function"""

    def wrapper(decor):
        decor.__name__ = func.__name__
        decor.__doc__ = func.__doc__
        decor.__original_func = func
        return decor

    return wrapper


def print_result(func):
    @save_original_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
