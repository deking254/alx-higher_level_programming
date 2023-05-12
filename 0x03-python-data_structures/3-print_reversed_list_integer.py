#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = -len(my_list)
    for liist in range(-1, length - 1, -1):
        print(my_list[liist])
