#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, (int, float)):
        string = str(number)
        print(string[-1], end="")
        return int(string[-1])
