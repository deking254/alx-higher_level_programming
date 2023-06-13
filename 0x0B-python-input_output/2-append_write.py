#!/usr/bin/python3
"""a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """the afrementioned function"""
    t = 0
    with open(filename, 'a') as fil:
        fil.write(text)
        fil.seek(0)
        return (len(text))
