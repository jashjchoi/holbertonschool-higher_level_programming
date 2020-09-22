#!/usr/bin/python3
"""file for task 2"""


class Square:
    """define size validation for class Square"""
    def __init__(self, size=0):
        """init private instance attribute"""
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
