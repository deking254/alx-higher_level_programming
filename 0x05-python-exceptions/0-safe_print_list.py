#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for number in range(0, x):
        try:
            if number == x - 1:
                print(my_list[number], end="\n")
            else:
                print(my_list[number], end="")
            i += 1
        except:
            print("")
            return (i)
    return (i)

