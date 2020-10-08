#!/usr/bin/python3
"""
    8-load_from_json_file
"""
import json


def load_from_json_file(filename):
    """Returns created object from a JSON file"""

    with open(filename, mode="r", encoding="UTF-8") as f:
        return json.load(f)
