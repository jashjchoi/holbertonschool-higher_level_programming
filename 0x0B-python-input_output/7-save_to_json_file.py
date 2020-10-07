#!/usr/bin/python3
"""
    7-save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file using a JSON"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
