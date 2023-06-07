#!/usr/bin/python3
"""a function that prints a square with the character"""


def print_square(size):
    """a function that prints a square with the character"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    else:
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            for _ in range(size):
                print("#" * size)
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
