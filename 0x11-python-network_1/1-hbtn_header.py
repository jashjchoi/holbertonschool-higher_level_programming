#!/usr/bin/python3
"""
takes in a URL, sends request to the URL
displays the value of the X-Request-Id variable
found in the header of the response
"""
from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    req = Request(argv[1])
    with urlopen(req) as response:
        header = response.info()
        print(header['X-Reqest-Id'])
