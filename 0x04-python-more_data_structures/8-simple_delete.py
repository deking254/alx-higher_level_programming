#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keys =  list(a_dictionary.keys())
    for ke in keys:
        if ke == key:
            a_dictionary.pop(key)
    return (a_dictionary)
