#!/usr/bin/python3
"""
    3-is_kind_of_class.py module
"""


def is_kind_of_class(obj, a_class):
    """
        Checks if the object is same instance of a class
        return: True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
