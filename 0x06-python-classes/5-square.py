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
            self.size = size

    @property
    def size(self):
        """size property"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area func"""
        return (self.__size ** 2)

    def my_print(self):
        """print func"""
        for _ in range(self.__size):
            if self.__size == 0:
                print("")
            else:
                print("#" * self.__size)
