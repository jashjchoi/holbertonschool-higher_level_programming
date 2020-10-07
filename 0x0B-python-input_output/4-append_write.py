#!/usr/bin/python3
"""
    4-append_write
"""


def append_write(filename="", text=""):
    """
        Append to file with text and returns the number of char added
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        if f.write(text):
            return len(text)
