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
    keys = method.__qualname__
    @wraps(method)
    def count(self, *args, **kwds):
        self._redis.incr(keys)
        return method(self, *args, **kwds)
    return count

def call_history(method: Callable) -> Callable:
    """ Call History decorator
    """
    keys = method.__qualname__
    input_list = keys + ":inputs"
    output_list = keys + ":inputs"
    @wraps(method)
    def call_list(self, *args, **kwds):
        self._redis.rpush(input_list, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(output_list, str(data))
        return data
    return call_list

class Cache:
    """ Defines Cache class
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

def replay(method: Callable):
    pass