#!/usr/bin/python3
"""
    9-rectangle module
"""


class Rectangle:
    """
        class Rectangle that defines a rectangle by: 8-rectangle.py
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init instances"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns whichever is bigger, rect_1 or rect_2"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with size"""
        height = width = size
        return cls(height, width)

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
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if i != self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """ Return a string representation of the rectangle"""
        r = "(" + str(self.__width) + ", " + str(self.__height) + ")"
        return self.__class__.__name__ + r

    def __del__(self):
        """ Print the message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
