#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """a instance method that prints the list, but sorted"""
        print(sorted(self))

