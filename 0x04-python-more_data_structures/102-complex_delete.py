#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    items = list(a_dictionary.items())
    for item in items:
        if item[1] == value:
            a_dictionary.pop(item[0])
    return (a_dictionary)
