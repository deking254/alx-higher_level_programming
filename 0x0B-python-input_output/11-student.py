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

    def to_json(self, attrs=None):
        new = self.__dict__.copy()
        found = []
        if type(attrs) == list:
            for i in attrs:
                status = 0
                if type(i) != str:
                    return(self.__dict__)
                else:
                    for j in list(self.__dict__.keys()):
                        if i == j:
                            status = 1;
                    if (status == 1):
                        found.append(i)
            if len(found) != 0:
                return {key: self.__dict__[key] for key in found}
        else:
            return(self.__dict__)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""


