#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
displays the body of the response (decoded in utf-8)
"""
import urllib.request
from sys import argv
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as f:
            res = f.read()
            print(res.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
