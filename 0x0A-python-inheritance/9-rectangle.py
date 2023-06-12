#!/usr/bin/python3
"""a rectangle class that inherits from base-geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """the rectangle class"""
    __width = None
    __height = None

    def __init__(self, width, height):
        """the init func"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """method that calculates the area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """handling the printf func"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
