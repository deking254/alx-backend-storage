#!/usr/bin/env python3
"""solves a question about redis"""
import redis
import uuid
import time
from typing import Callable, Union
from functools import wraps


def call_history(method: Callable) -> Callable:
    """a decorator for cache for storing input and output"""
    @wraps(method)
    def initialize_history(self, data) -> Callable:
        """this function initializes the lists"""
        uid = method(self, data)
        redis_instance = self._redis
        self._redis.rpush(method.__qualname__ + ":inputs",
                          (self.get(uid)))
        self._redis.rpush(method.__qualname__ + ":outputs", uid)
        return uid
    return initialize_history


def count_calls(method: Callable) -> Callable:
    """a decorator for class cache that returns callable to use"""
    @wraps(method)
    def incrementor(self, data) -> Callable:
        """keeps track of the count"""
        start_time = int(time.time())
        redis_instance = self._redis
        if redis_instance.get(method.__qualname__) is not None:
            redis_instance.incr(method.__qualname__)
        else:
            redis_instance.set(self.store.__qualname__, 1)
        redis_instance.expireat(self.store.__qualname__, start_time + 10)
        a = method(self, data)
        return a
    return incrementor


class Cache:
    """class to generate a cache class"""
    _redis = None

    def __init__(self):
        """creates a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """generate a random key"""
        uid = str(uuid.uuid1())
        self._redis.set(uid, data)
        return uid

    def get(self, key: str,
            fn: Callable = None) -> Union[str, int, float, bytes]:
        """returns the value at the key"""
        a = self._redis.get(key)
        if (fn is not None):
            if fn == str:
                return self.get_str(key)
            elif fn == int:
                return self.get_int(key)
            else:
                return fn(a)
        else:
            return a

    def get_str(self, key: str) -> str:
        """returns a string from the server"""
        try:
            a = self.get(self, key).decode("utf-8")
            return a
        except Exception as e:
            return e

    def get_int(self, key: int) -> int:
        """returns an int from server"""
        try:
            b = self._redis.get(key).decode()
            return int(b)
        except Exception as e:
            return e

    def replay(self, key: Union[str, int, float, bytes]) -> None:
        """breaks down the IO operations"""
        inputs = self._redis.lrange(key.__qualname__ + ":inputs", 0, -1)
        outputs = self._redis.lrange(key.__qualname__ + ":outputs", 0, -1)
        input_output = list(zip(inputs, outputs))
        count = int(self._redis.get(key.__qualname__))
        print('{} was called {} times:'.format(key.__qualname__, count))
        for i in input_output:
            print('{}(*({},)) -> {}'.format(key.__qualname__,
                  i[0].decode(), i[1]))
