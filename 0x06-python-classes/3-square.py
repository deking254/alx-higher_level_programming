#!/usr/bin/python3
"""This is a module for greeting and performing square calculations."""


class Square:
    """square class"""
    __size = None

    def __init__(self, size=0):
        """init func"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area func"""
        return (self.__size ** 2)
