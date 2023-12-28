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
        key = 'count:' + url
        cache = cache.Redis()
        cache.incr(f'count:{url}')
        if cache.get(f'{url}'):
            return cache.get(f'{url}').decode()

        response = method(url)
        cache.set(f'{url}', response, ex=10)
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
