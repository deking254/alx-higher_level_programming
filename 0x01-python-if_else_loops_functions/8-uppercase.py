#!/usr/bin/python3
def uppercase(str):
    for l in str:
        if ord(l) >= 97 and ord(l) <= 122:
            lower = 1
        if ord(l) >= 65 and ord(l) <= 90:
            lower = 0
        if ord(l) == 32:
            lower = 0
        print("{}".format(chr(ord(l) - 32) if lower else l), end="")
    print("{}".format(''), end="\n")
