from functools import wraps
from hashlib import sha256
import time
from typing import Any, Callable


class CachedData:
    data: dict = {}


def cache_request(expires: int):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            key_data = (func.__name__, args, frozenset(kwargs.items()))
            key = sha256(str(key_data).encode()).hexdigest()

            current_time = time.time()
            if key in CachedData.data:
                cached_value, timestamp = CachedData.data[key]
                if current_time - timestamp < expires:
                    return cached_value

            result = await func(*args, **kwargs)
            CachedData.data[key] = (result, current_time)
            return result

        return wrapper
    return decorator
