#!/usr/bin/env python3
""" This module 
"""
from functools import wraps
from typing import Callable, Optional, Union
import uuid
import redis


def count_calls(method: Callable) -> Callable:
    """ Count number of calls to methods used
    """
    number = method.__qualname__
    @wraps(method)
    def count(self, *args, **kwds):
        self._redis.incr(number)
        return method(self, *args, **kwds)
    return count
    
class Cache:
    """ Defines Cache class
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get( self, key, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        
        data = self._redis.get(key)
        if not fn:
            return data
        else:
            return fn(data)
    
    def get_str(self):
        pass

    def get_int(self):
        pass

