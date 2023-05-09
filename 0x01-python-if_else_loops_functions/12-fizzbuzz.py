#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0:
            if n % 5 == 0:
                print("FizzBuzz", end=", ")
            else:
                print("Fizz", end=", ")
        if n % 5 == 0 and n != 100:
            if n % 3 == 0:
                print("FizzBuzz", end=", ")
            else:
                print("Buzz", end=", ")
        if n % 3 != 0 or n % 5 != 0 or n != 100:
            print("{}".format(n), end=", ")
        if n == 100:
            print("{}".format("Buzz"), end=" ")

