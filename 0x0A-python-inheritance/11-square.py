#!/usr/bin/python3
"""
    11-square.py module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """init method"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """print the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
