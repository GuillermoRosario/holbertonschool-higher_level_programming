#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    print("{1} is positive".format(number))
elif number == 0:
    print("{0} is zero".format(number))
elif number < 0:
    print("{-1} is negative".format(number))
