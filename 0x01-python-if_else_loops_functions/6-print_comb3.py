#!/usr/bin/python3
for numb1 in range(0, 9):
    for numb2 in range(1, 10):
        if numb1 != numb2 and numb2 > numb1:
            if numb1 == 8 and numb2 == 9:
                print("{}{}".format(numb1, numb2), end="\n")
            else:
                print("{}{}".format(numb1, numb2), end=", ")
