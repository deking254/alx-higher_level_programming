#!/usr/bin/python3
"""module to add attr to object"""


def add_attribute(obj, attr="", val=""):
    """a function that adds a new attribute to an objec"""
    obj.__setattr__(attr, val)
