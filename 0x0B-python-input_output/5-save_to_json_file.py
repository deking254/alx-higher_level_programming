#!/usr/bin/python3
"""a function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file"""
    with open(filename, 'w') as fle:
        fle.write(json.dumps(my_obj))
