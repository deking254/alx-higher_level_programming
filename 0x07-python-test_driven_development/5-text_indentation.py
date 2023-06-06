#!/usr/bin/python3
"""
    a function that prints a 
    text with 2 new lines 
    after each of these 
    characters: ., ? and :
"""

def text_indentation(text):
    """
        the function that
        prints the newline
        after the charaters stated
    """
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
