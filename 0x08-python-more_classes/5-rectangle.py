#!/usr/bin/python3
"""
    5-rectangle module
"""


class Rectangle:
    """
        class Rectangle that defines a rectangle by: 4-rectangle.py
    """

    def __init__(self, width=0, height=0):
        """Init instances"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """__str__ method funtion to return rectangle with the char # """
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect

        for i in range(self.__height):
            if i == self.__height - 1:
                rect += ('#' * self.__width)
            else:
                rect += (('#' * self.__width) + '\n')
        return rect

    def __repr__(self):
        """ Return a string representation of the rectangle"""
        r = "(" + str(self.__width) + ", " + str(self.__height) + ")"
        return self.__class__.__name__ + r

    def __del__(self):
        """ Print the message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
