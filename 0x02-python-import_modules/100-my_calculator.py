#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    argumentslen = len(sys.argv[1:])
    arguments = sys.argv[1:]
    if argumentslen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argumentslen == 3:
        a = int(arguments[0])
        b = int(arguments[2])
        opr = arguments[1]
        if arguments[1] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        if arguments[1] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if arguments[1] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        if arguments[1] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        elif(opr != '+' and opr != '-' and opr != '*' and opr != '/'):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
