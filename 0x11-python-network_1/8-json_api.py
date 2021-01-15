#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        r = requests.post(url, data={'q': argv[1]})
    else:
        r = requests.post(url, data={'q': ""})
    try:
        js_obj = r.json()
        if js_obj:
            print("[{}] {}".format(js_obj.get("id"), js_obj.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
