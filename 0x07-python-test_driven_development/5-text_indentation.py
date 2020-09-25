#!/usr/bin/python3
"""
    text_indentation module
    prints a text with 2 newlines after each ['.', '?', ':']
    Return None
"""


def text_indentation(text):
    """ prints "text" with 2 newlines after each of these char: ['.', '?', ':']
        checks if "text" is a str
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
