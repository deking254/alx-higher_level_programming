#!/usr/bin/python3
"""the function that prints the newline after the charaters stated"""


def text_indentation(text):
    """the function that prints the newline after the charaters stated"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        mod = text.replace(". ", ".")
        mod = mod.replace("? ", "?").replace(": ", ":")
        for lin in mod:
            if lin == "." or lin == "?" or lin == ":":
                print(lin)
                print("")
            else:
                print(lin, end="")
