#!/usr/bin/python3
"""
    2-read_lines
"""


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file"""
    line_num = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line_num < nb_lines or not nb_lines or nb_lines < 0:
                print(line, end="")
            line_num += 1
