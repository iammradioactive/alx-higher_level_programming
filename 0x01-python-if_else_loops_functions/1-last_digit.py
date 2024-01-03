#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if number < 0:
    last_digit = -last_digit

open_str = "Last digit of {} is {} "

if last_digit > 5:
    print(open_str.format(number, last_digit) + "and is greater than 5")
elif last_digit == 0:
    print(open_str.format(number, last_digit) + "and is 0")
else:
    print(open_str.format(number, last_digit) + "and is less than 6 and not 0")
