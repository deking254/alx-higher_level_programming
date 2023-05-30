#!/usr/bin/python3
def area(self):
    return (self ** 2)
class Square:
    __size = None
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        return (self.__size ** 2)
