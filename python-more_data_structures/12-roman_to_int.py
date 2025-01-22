#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev = 0
    if roman_string:
        return 0
    if roman_string:
        for char in reversed(roman_string):
            if char in roman:
                value = roman[char]
                if value < prev:
                    result -= value
                else:
                    result += value
                    prev = value
        return int(result)
