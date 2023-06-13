#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """the function itself"""
    with open("my_file_0.txt", "r") as file:
        ft = file.read()
        print(ft, end="")
