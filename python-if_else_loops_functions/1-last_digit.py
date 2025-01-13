#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = 10
if number < 0:
    mod = -10
if number % mod == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif number % mod > 5:
    print(f"Last digit of {number} is {number % mod} and is greater than 5")
elif number % mod < 6 and number % mod != 0:
    print(f"Last digit of {number} is {number % mod} and is\
 less than 6 and not 0")
