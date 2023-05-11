#!/usr/bin/python3
import sys
if __name__ == '__main__':
    arguments = len(sys.argv) - 1
    i = 1
    if arguments == 0:
        print("{} arguments.".format(arguments))
    if arguments == 1:
        print("{} argument:".format(arguments))
        print("{} {}".format(1, sys.argv[1]))
    if arguments > 1:
        print("{} arguments:".format(arguments))
        for argument in sys.argv[1:]:
            print("{} {}".format(i, argument))
            i += 1
