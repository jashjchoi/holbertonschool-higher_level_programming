#!/usr/bin/python3
"""
takes Github credentials (username and pw)
and uses the Github API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    usrname = argv[1]
    pw = argv[2]
    req = requests.get("https://api.github.com/user", auth=(usrname, pw))
    print(req.json().get("id"))
