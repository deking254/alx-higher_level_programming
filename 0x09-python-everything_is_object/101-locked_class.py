#!/usr/bin/python3
class LockedClass:
    def __init__(self):
        self.__slots__ = ("first_name")
