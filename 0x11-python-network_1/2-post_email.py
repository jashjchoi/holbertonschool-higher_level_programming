#!/usr/bin/python3
"""
takes in a URL and an email
sends a POST request to the passed URL
with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
from sys import argv
import urllib.parse

if __name__ == "__main__":
    mail = {'email': argv[2]}
    data = urllib.parse.urlencode(mail)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))
