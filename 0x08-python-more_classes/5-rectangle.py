#!/usr/bin/python3
"""
    c class for rectangle
"""


class Rectangle:
    """
        the rectaangle class
    """
    __width = None
    __height = None
    def __init__(self, width=0, height=0):
        """
            the rectaangle class
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """
            the width getter
        """
        return (self.__width)
    @width.setter
    def width(self, value):
        """
            the width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
    @property
    def height(self):
        """
            the height getter
        """
        return (self.__height)
    @height.setter
    def height(self, value):
        """
            the height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
    def area(self):
        """
            a function of the class that 
            calculates the area of a rectangle
        """
        return (self.__height * self.__width)
    def perimeter(self):
        """
            a function of the rectangle class 
            that calculates the perimeter
            of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (2 * self.__height + 2 * self.__width)
    def __str__(self):
        """
            the str function to return the string
            representation of a class
        """
        new = ""
        for t in range(self.__height):
            if t != self.__height - 1:
                new += "#" * self.__width + "\n"
            else:
                new += "#" * self.__width
        return (new)
    def __repr__(self):
        """
            the representation function of 
            the rectangle class
        """
        return ("Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")")
    def __del__(self):
        """
            the representation function of 
            the rectangle class
        """
        print("Bye rectangle...")

