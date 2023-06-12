#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance of a class that inherited"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
