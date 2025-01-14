#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        digit = number % -10 * -1
    else:
        digit = number % 10
    print(f"{digit}", end="")
    return digit
