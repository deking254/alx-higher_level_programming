#!/usr/bin/python3
"""the function that prints the newline after the charaters stated"""


def text_indentation(text):
    """the function that prints the newline after the charaters stated"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        mod = text.replace(". ", ".").replace(", ", ".").replace("? ", "?").replace(": ", ":")
        for l in mod:
            if l == "." or l == "?" or l == ":":
                print(l)
                print("")
            else:
                print(l, end="")
