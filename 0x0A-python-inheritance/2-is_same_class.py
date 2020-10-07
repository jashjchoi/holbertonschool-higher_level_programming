#!/usr/bin/python3
"""
    2-is_same_class module
"""


def is_same_class(obj, a_class):
    """
        checks if the object is same instance of the specified class
        return: true or false
    """
    if isinstance(a_class(), type(obj)):
        return True
    else:
        return False
