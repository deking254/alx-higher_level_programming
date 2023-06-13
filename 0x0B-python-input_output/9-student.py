#!/usr/bin/python3
"""a class module for a student"""


class Student:
    """the student class"""
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        """the init func"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return(self.__dict__)
