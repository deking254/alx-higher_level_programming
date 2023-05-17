#!/user/bin/python3
def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    arr = [None] * len(roman_string)
    if len(roman_string) > 1:
        if romans.get(roman_string[0]) < romans.get(roman_string[1]):
            return (total)
