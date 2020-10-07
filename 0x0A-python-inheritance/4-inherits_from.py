#!/usr/bin/python3
"""
    4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    checks if object is an instance of a class that inherited\
        from the specified class.
    return: True or False
    """

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
