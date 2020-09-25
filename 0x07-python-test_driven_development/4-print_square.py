#!/usr/bin/python3
"""
    4-print_square.py module
    prints a square with the character #.
    return None
"""


def print_square(size):
    """ prints a square depending on the "size" parameter
        return None
    """
    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for row in range(size):
        print('#' * size)
