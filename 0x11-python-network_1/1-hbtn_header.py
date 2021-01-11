#!/usr/bin/python3
"""
takes in a URL, sends request to the URL
displays the value of the X-Request-Id variable
found in the header of the response
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen("{}".format(argv[1])) as res:
        header = res.info()
        print(header['X-Request-Id'])
