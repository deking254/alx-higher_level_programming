#!/usr/bin/python3
"""this module implemetns a square class"""


Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """the squre class"""
    _size = None

    def __init__(self, size):
        """init function"""
        self.integer_validator("size", size)
        self._size = size

    def area(self):
        """method that calculates the are of a square by multiplying size by itself"""
        return (self._size ** 2)

    def __str__(self):
        return ("[Rectangle] " + str(self._size + "/" + str(self._size)))
