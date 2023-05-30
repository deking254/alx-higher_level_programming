#!/usr/bin/python3
"""This is a module for greeting and performing square calculations."""


class Square:
    """square class"""
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """init func"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__position = position
            self.__size = size

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

    @property
    def position(self):
        """position prop"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """position setter"""
        info = "position musti be a tuple of 2 positive integers"
        if type(value) is tuple and len(value) == 2:
            if type(value[0]) is int and type(value[1]) is int:
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    raise TypeError(info)
        else:
            raise TypeError(info)

    def area(self):
        """area func"""
        return (self.__size ** 2)

    def my_print(self):
        """print #"""
        if self.__size == 0:
            print("")
        for l in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
