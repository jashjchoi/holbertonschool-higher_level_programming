#!/usr/bin/python3
"""
    3-write_file
"""


def write_file(filename="", text=""):
    """returns the number of characters written"""

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
