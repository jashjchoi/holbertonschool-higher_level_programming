#!/usr/bin/python3
"""file for task 3"""


class Square:
    """define class Square with area method"""
    def __init__(self, size=0):
        """init private instance attribute"""
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
