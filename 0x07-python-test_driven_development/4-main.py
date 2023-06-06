#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

def checker(t):
    try:
        print_square(t)
    except Exception as e:
        print(e)
