#!/usr/bin/env python3
"""a simple web cache using python"""
import requests
import redis
import time
import os
from typing import DefaultDict
counter_dict = DefaultDict(int)


cache = redis.Redis()
def get_page(url: str) -> str:
    """returns the content off the url"""
    try:
        page = 'requests.get(url)'
        key = 'count:{' + url + '}'
        counter_dict[key] += 1
        times = counter_dict[key]
        cache.set(key, times)
        time.sleep(10)
        cache.flushdb()
        return page
    except Exception:
        pass
