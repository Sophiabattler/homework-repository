"""Task01 - Cache n times"""


def make_key(*args, **kwargs):
    """ """
    keys = []

    def deep_hash_search(items):
        for item in items:
            if not item.__hash__:
                keys.append(str(item))
            elif item.__hash__ and type(item) != int and len(item) > 1:
                return deep_hash_search(item)
            else:
                keys.append(item)

    deep_hash_search(args)
    return tuple(keys), frozenset(sorted(kwargs.items()))


def cache(times=2):
    def wrapper(func):
        cached_value = {}

        def inner(*args, **kwargs):
            key = make_key(args, kwargs)
            if key not in cached_value:
                res = func(*args, **kwargs)
                cached_value[key] = [res, 0]
            res, called = cached_value[key]
            if called > times:
                return func(*args, **kwargs)
            else:
                cached_value[key][1] += 1
                return res

        return inner

    return wrapper
