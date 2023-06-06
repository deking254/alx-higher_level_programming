#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

def checker(f, l):
    try:
        say_my_name(f, l)
    except TypeError as e:
        print(e)
