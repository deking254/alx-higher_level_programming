#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberstr = str(number)
if number >= 0:
    n = int(numberstr[-1])
    if int(numberstr[-1]) > 5:
        print(f"Last digit of {number} is {n} and is greater than 5")
    if int(numberstr[-1]) < 6 and int(numberstr[-1]) != 0:
        print(f"Last digit of {number} is {n} and is less than 6 and not 0")
    if int(numberstr[-1]) == 0:
        print(f"Last digit of {number} is {n} and is 0")
if number < 0:
    nega = int(numberstr[-1]) * -1
    if int(numberstr[-1]) * -1 > 5:
        print(f"Last digit of {number} is {nega} and is greater than 5")
    if int(numberstr[-1]) * -1 < 6 and int(numberstr[-1]) * -1 != 0:
        print(f"Last digit of {number} is {nega} and is less than 6 and not 0")
    if int(numberstr[-1]) == 0:
        print(f"Last digit of {number} is {numberstr[-1]} and is 0")
