#!/usr/bin/python3
"""
    10-class_to_json
"""


def class_to_json(obj):
    """Returns the dictionary description for JSON
    """

    return obj.__dict__
