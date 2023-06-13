#!/usr/bin/python3
"""module to make JSON"""
import json


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object"""
    return(json.dumps(my_obj))
