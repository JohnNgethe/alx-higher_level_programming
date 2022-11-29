#!/usr/bin/python3

"""
Print all possible different combinations of two digits in ascending order.
The two digits must be different - 01 and 10 are considered identical.
"""
for digit_1 in range(0, 10):
    for digit_2 in range(digit_1 + 1, 10):
        if digit_1 == 8 and digit_2 == 9:
            print("{}{}".format(digit_1, digit_2))
        else:
            print("{}{}".format(digit_1, digit_2), end=", ")
