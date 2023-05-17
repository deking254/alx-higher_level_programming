#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    else:
        arr = [None] * len(roman_string)
        if len(roman_string) > 1:
            for i in range(0, len(roman_string)):
                arr[i] = romans.get(roman_string[i])
            for r in range(0, len(roman_string)):
                if r != len(roman_string) - 1:
                    if arr[r] < arr[r + 1]:
                        arr[r] *= -1
            for num in arr:
                total += num
            return (total)
        if len(roman_string) == 1:
            return (romans.get(roman_string[0]))
