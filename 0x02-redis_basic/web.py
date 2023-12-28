#!/usr/bin/env python3
"""a simple web cache using python"""
import requests
import redis
import time
import os
from typing import Callable


def counter(method: Callable) -> str:
    """does the adding of the url counter"""
    def increment(url):
        """adds to the url count"""
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = method(url)
        client.set(f'{url}', response, 10)
        return response
    return increment
        
@counter
def get_page(url: str) -> str:
    """returns the content off the url"""
    try:
        page = requests.get(url)
        return page.text
    except Exception as e:
        pass
