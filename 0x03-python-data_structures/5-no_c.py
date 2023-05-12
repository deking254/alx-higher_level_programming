#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for my_strin in my_string:
        if my_strin != "c" and my_strin != "C":
            newstring += my_strin
    return (newstring)
