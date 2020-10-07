#!/usr/bin/python3
"""
    1-number_of_lines
"""


def number_of_lines(filename=""):
    """Reads a text file andreturns the number of lines"""
    with open(filename, encoding="utf-8") as f:
        line_num = 0
        for line in f:
            line_num += 1
    return line_num
