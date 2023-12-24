#!/usr/bin/env python3
"""a simple web cache using python"""
import requests
import redis
import time
import os
from typing import DefaultDict
counter_dict = DefaultDict(int)
cache = redis.Redis()


def counter(self):
    """does the adding of the url counter"""
    def increment(url):
        """adds to the url count"""
        key = 'count:' + url
        start_time = time.time()
        cache.incr(key)
        cache.expireat(key, int(start_time) + 10)
        return self(url)
    return increment
        
@counter
def get_page(url: str) -> str:
    """returns the content off the url"""
    try:
        page = requests.get(url)
        return page
    except Exception as e:
        pass
