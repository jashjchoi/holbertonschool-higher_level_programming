#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
displays the value of X-Request-Id in the response header
"""
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers.get('X-Request-Id'))
