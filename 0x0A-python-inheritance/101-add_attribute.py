#!/usr/bin/python3
"""module to add attr to object"""


def add_attribute(obj, attr="", val=""):
    """a function that adds a new attribute to an objec"""
    if hasattr(obj, '__dict__'):
        obj.__setattr__(attr, val)
    else:
        raise TypeError("can't add new attribute")
