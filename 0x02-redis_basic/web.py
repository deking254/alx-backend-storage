#!/usr/bin/env python3
"""a simple web cache using python"""
import requests
import redis
import time
import os
from typing import Callable
from functools import wraps
client = redis.Redis()

print(dir(client.set('er', "ty")))
def counter(method: Callable) -> str:
    """does the adding of the url counter"""
    @wraps(method)
    def increment(url):
        """adds to the url count"""
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = method(url)
        client.set(f'{url}', response, ex=10)
    return increment
        
@counter
def get_page(url: str) -> str:
    """returns the content off the url"""
    try:
        page = requests.get(url)
        return "page.text"
    except Exception as e:
        pass
