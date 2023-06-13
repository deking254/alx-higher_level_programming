#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """the function itself"""
    with open(filename, 'r') as fil:
        ft = fil.read()
        print(ft, end="")
