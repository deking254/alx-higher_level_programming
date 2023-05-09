#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberstr = str(number)
if int(numberstr[-1]) > 5:
    print(f"Last digit of {number} is {numberstr[-1]} and is greater than 5")
if int(numberstr[-1]) < 6 and int(numberstr[-1]) != 0:
    print(f"Last digit of {number} is {numberstr[-1]} and is less than 6 and not 0")
if int(numberstr[-1]) == 0:
    print(f"Last digit of {number} is {numberstr[-1]} and is 0")
