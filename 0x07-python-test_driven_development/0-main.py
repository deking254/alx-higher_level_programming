#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

def checker(a, b=98):
    try:
        print(add_integer(a, b))
    except Exception as e:
        print(e)
