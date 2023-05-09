#!/usr/bin/python3
def remove_char_at(st, n):
    i = 0
    string = ""
    for s in st:
        if i == n:
            i += 1
        else:
            string += s
        i += 1
    return string
