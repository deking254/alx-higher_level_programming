#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            lower = 1
        if ord(letter) >= 65 and ord(letter) <= 90:
            lower = 0
        if ord(letter) < 65 or ord(letter) > 122:
            lower = 0
        print("{}".format(chr(ord(letter) - 32) if lower else letter), end="")
    print("{}".format(''), end="\n")
