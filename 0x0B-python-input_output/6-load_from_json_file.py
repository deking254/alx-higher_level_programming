#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """the aforementioned func"""
    with open(filename, 'r') as fle:
        content = fle.read()
        return (json.loads(content))
