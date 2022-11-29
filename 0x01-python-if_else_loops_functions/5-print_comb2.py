#!/usr/bin/python3

'''
Prints numbers from 0 to 99 separated by , followed by a space
in ascending order and with two digits and the last number
should be followed by a new line'''
for number in range(0, 100):
    if number == 99:
        print(f"{number}")
    else:
        print("{:02}".format(number), end=", ")
