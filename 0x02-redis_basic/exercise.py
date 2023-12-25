#!/usr/bin/env python3
"""solves a question about redis"""
import redis
import uuid
from typing import Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """a decorator for class cache that returns callable to use"""
    print(wraps(method).func)
    def incrementor(self, data):
        """keeps track of the count"""
        self._redis.incr(method.__qualname__)
        return method(self, data)
    return incrementor


def call_history(method: Callable) -> Callable:
    """a decorator for cache for storing input and output"""
    def initialize_history(self, data):
        """this function initializes the lists"""
        self._redis.rpush(method.__qualname__ + ":inputs", data)
        self._redis.set(method.__qualname__ + ":outputs", '')
        return method(self, data)
    return initialize_history


class Cache:
    """class to generate a cache class"""
    _redis = None

    def __init__(self):
        """creates a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: str or int or float or bytes) -> str:
        """generate a random key"""
        self._redis.set(self.store.__qualname__, 0)
        uid = str(uuid.uuid1())
        self._redis.set(uid, data)
        self._redis.rpush(self.store.__qualname__ + ":inputs", data)
        self._redis.rpush(self.store.__qualname__ + ":outputs", uid)
        return uid

    def get(self, key: str, fn: Callable = None) -> str or int or float or bytes:
        """returns the value at the key"""
        count_calls(self)
        self._redis.incr(self.get.__qualname__)
        try:
            a = self._redis.get(key)
            if (fn is not None):
                return fn(a)
            else:
                return a
        except Exception as e:
            return e

    def get_str(self, key: str) -> str:
        """returns a string from the server"""
        return self.get(self, key, str)

    def get_int(self, key: int) -> int:
        """returns an int from server"""
        return self.get(self, key, int)

    def replay(self, key: str or int or float or bytes):
        """breaks down the IO operations"""
        print(self._redis.get(self.store.__qualname__))
        inputs = self._redis.lrange(key.__qualname__ + ":inputs", 0, -1)
        outputs = self._redis.lrange(key.__qualname__ + ":outputs", 0, -1)
        input_output = list(zip(inputs, outputs))
        count = int(self._redis.get(self.store.__qualname__))
        print('{} was called {} times:'.format(key.__qualname__, count))
        for i in input_output:
            print('{}(*({},)) -> {}'.format(key.__qualname__, i[0], i[1]))
