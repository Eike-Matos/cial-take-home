from functools import lru_cache

@lru_cache(maxsize=128)
def cached(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper