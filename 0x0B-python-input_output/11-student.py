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
        ne = self.__dict__
        if type(attrs) == list:
            for i in attrs:
                if type(i) != str:
                    return(self.__dict__)
            return {key: di[key] for key in attrs if key in di}
        else:
            return(self.__dict__)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if json.get("first_name") is not None:
            self.first_name = json.get("first_name")
        if json.get("last_name") is not None:
            self.last_name = json.get("last_name")
        if json.get("age") is not None:
            self.age = json.get("age")
