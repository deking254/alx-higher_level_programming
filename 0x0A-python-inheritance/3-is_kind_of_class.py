#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
