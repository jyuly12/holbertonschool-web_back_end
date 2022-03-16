#!/usr/bin/env python3
""" this module use redis in other exercise
"""
import redis
import requests
r = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """ get_page function
    """
    r.set(f"cached:{url}", count)
    resp = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
