#!/usr/bin/python3
""" matrix_divided divides the given matrix
by the parameter "div", and returns the divided matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix by an int or float
        returns new matrix containing the list of divided numbers
    """
    me1 = "matrix must be a matrix (list of lists) of integers/floats"
    me2 = "Each row of the matrix must have the same size"
    result = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(me2)
        inner_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(me1)
            else:
                inner_list.append(round(items / div, 2))
        result.append(inner_list)

    return result
