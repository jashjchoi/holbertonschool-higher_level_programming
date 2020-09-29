#!/usr/bin/python3
"""
    1-rectangle module
"""


class Rectangle:
    """
    class Rectangle defines a rectangle by: 0-rectangle
    """

    def __init__(self, width=0, height=0):
        """ Init instances"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """ getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
