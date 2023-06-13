#!/usr/bin/python3
"""a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """the afrorementioned function"""
    with open(filename, "w+", encoding='utf-8') as f:
        u = 0
        f.write(text)
        f.seek(0)
        ft = f.read()
        for i in ft:
            u += 1
        return (u)
