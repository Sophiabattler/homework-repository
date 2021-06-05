"""Task03 - Filter"""
from functools import partial


class Filter:
    """Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria"""

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(func(item) for func in self.functions)]


def make_filter(**kwargs):
    """Generate filter object for specified keywords"""
    filter_funcs = []

    for key, value in kwargs.items():

        def keyword_filter_func(data, key, value):
            """
            There was got only 'value' as an argument, what did not let to
            understand whether the data has a certain 'key' with certain 'value'
            After corrections 'keyword_filter_func' gets data and checks
            if data has specified pair 'key-value'
            """
            return data.get(key) == value

        filter_func_with_key_and_value = partial(
            keyword_filter_func, key=key, value=value
        )
        filter_funcs.append(filter_func_with_key_and_value)

    return Filter(filter_funcs)
