#!/usr/bin/python3
"""a rectangle class that inherits from base-geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """the rectangle class"""
    _width = None
    _height = None

    def __init__(self, width, height):
        """the init func"""
        try:
            self.integer_validator("height", height)
            self._width = width
            self._height = height
        except Exception as e:
            return
        try:
            self.integer_validator("width", width)
            self._width = width
        except Exception:
            return
