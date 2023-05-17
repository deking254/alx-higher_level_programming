#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    if not isinstance(roman_string, str):
        return (0)
    else:
        arr = [None] * len(roman_string)
        if len(roman_string) > 1:
            if romans.get(roman_string[0]) < romans.get(roman_string[1]):
                arr[0] = romans.get(roman_string[0]) * -1
                for i in range(1, len(roman_string)):
                    arr[i] = romans.get(roman_string[i])
                for num in arr:
                    total += num
                return (total)
            else:
                for i in range(0, len(roman_string)):
                    arr[i] = romans.get(roman_string[i])
                for num in arr:
                    total += num
                return (total)
        if len(roman_string) == 1:
            return (romans.get(roman_string[0]))
