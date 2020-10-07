#!/usr/bin/python3
"""
    0-lookup module
"""


def lookup(obj):
    """returns the list of available attributes and methods of obj"""
    return [method_name for method_name in dir(obj)]
