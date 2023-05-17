#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.items())
    for so in sort:
        print("{}: {}".format(so[0], so[1]))
