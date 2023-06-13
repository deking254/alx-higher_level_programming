#!/usr/bin/python3
"""module for JSON"""
import json


def from_json_string(my_str):
    """a function that returns an object (Python data structure)"""
    return (json.loads(my_str))
