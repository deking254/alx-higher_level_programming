#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for number in range(0, x):
        try:
            print("{:d}".format(my_list[number]), end="")
            i += 1
        except (ValueError, TypeError):
            if TypeError == IndexError:
                print(TypeError)
                return (i)
            continue
    print("")
    return (i)
