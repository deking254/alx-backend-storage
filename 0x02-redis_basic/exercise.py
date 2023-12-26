#!/usr/bin/env python3
"""solves a question about redis"""
import redis
import uuid
import time
from typing import Callable
from functools import wraps

def call_history(method: Callable) -> Callable:
    """a decorator for cache for storing input and output"""
    @wraps(method)
    def initialize_history(self, data) -> Callable:
        """this function initializes the lists"""
        uid = method(self, data)
        redis_instance = self._redis
        self._redis.rpush(self.store.__qualname__ + ":inputs", self._redis.get(uid))
        self._redis.rpush(self.store.__qualname__ + ":outputs", uid)
        return uid
    return initialize_history

def count_calls(method: Callable) -> Callable:
    """a decorator for class cache that returns callable to use"""
    @wraps(method)
    def incrementor(self, data) -> Callable:
        """keeps track of the count"""
        start_time = int(time.time())
        redis_instance = self._redis
        if redis_instance.get(self.store.__qualname__) is not None:
            redis_instance.incr(self.store.__qualname__)
            
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
    def store(self, data: str or int or float or bytes) -> str:
        """generate a random key"""
        uid = str(uuid.uuid1())
        self._redis.set(uid, data)
        return uid

    def get(self, key: str, fn: Callable = None) -> str or int or float or bytes:
        """returns the value at the key"""
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

    def replay(self, key: str or int or float or bytes) -> None:
        """breaks down the IO operations"""
        inputs = self._redis.lrange(key.__qualname__ + ":inputs", 0, -1)
        outputs = self._redis.lrange(key.__qualname__ + ":outputs", 0, -1)
        input_output = list(zip(inputs, outputs))
        count = int(self._redis.get(key.__qualname__))
        print('{} was called {} times:'.format(key.__qualname__, count))
        for i in input_output:
            print('{}(*({},)) -> {}'.format(key.__qualname__, i[0], i[1]))
