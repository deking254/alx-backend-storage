#!/usr/bin/env python3
"""a simple web cache using python"""
import requests
import redis
import time
import os
from typing import Callable
cache = redis.Redis()


def counter(method: Callable) -> str:
    """does the adding of the url counter"""
    def increment(url):
        """adds to the url count"""
        key = 'count:' + url
        cache.incr(key)
        count = cache.get(key).decode()
        cache.set(key, count, ex=10)
        return method(key)
    return increment
        
@counter
def get_page(url: str) -> str:
    """returns the content off the url"""
    try:
        page = requests.get(url)
        return page.text
    except Exception as e:
        pass
