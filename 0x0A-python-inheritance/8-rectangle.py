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
        self._width = width
        self._height = height
