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
