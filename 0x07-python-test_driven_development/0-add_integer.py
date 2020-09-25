#!/usr/bin/python3
"""
    0_add_integer module
    add_integer: adds two integers
    return a + b
"""


def add_integer(a, b=98):
    """ Function that adds 2 integers
        return a + b
    """

    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    if isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return int(a + b)
