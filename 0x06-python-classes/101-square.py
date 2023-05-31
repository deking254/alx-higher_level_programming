#!/usr/bin/python3
""""This is the square module"""


class Square:
    """square class"""
    __size = None
    __position = None

    @property
    def size(self):
        """size getter"""
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
        """position property"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """position setter"""
        f = "position must be a tuple of 2 positive integer"
        if type(value) is tuple and len(value) == 2:
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError(f)
        else:
            raise TypeError("position must be a tuple of 2 positive integer")

    def __init__(self, size=0, position=(0, 0)):
        """init func"""
        self.size = size
        self.position = position

    def area(self):
        """area func"""
        return (self.__size ** 2)

    def my_print(self):
        """my print func"""
        values = []
        if self.__size == 0:
            values.append("" + "\n")
            return(str(values))
        for _ in range(self.__position[1]):
            values.append("" + "\n")
        for i in range(0, self.__size):
            values.append(" " * self.__position[0])
            if i != self.__size - 1:
                values.append("#" * self.__size + '\n')
            else:
                values.append("#" * self.__size)
        return ("".join(values))

    def __str__(self):
        """the string func"""
        return(self.my_print())
