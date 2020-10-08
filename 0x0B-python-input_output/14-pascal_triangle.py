#!/usr/bin/python3
"""
    14-pascal_triangle
"""


def pascal_triangle(n):
    """
        returns a list of lists of int representing Pascals triangle of n
    """
    if n <= 0:
        return []
    result = []

    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(result[-1][j:j + 2]))
        result.append(row)
    return result
