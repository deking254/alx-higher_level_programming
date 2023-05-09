#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        print(f"{ord(letter)- 32:c}" if ord(letter)>=97 and ord(letter)<=122 else f"{letter}", end="")
    print('',end="\n")
