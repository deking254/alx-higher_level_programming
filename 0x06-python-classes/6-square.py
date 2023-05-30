#!/usr/bin/python3


class Square:
    __size = None
    __position = None
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__position = position
            self.__size = size
    @property
    def size(self):
        return (self.__size)
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    @property
    def position(self):
        return (self.__position)
    @position.setter
    def position(self, value):
        if type(value) is not tuple(2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def area(self):
        return (self.__size ** 2)
    def my_print(self):
        for _ in range(self.__size):
            if self.__size == 0:
                print(" " * self.__position[0], end="")
                print("")
            else:
                print(" " * self.__position[0], end="")    
                print("#" * self.__size)
