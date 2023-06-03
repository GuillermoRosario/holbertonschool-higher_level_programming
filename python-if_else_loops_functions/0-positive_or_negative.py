#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for randint in range (-10,10):
    print(randint, end=" ")
    if randint > 0:
        print("is positive")
    if randint == 0:
        print("is zero")
    elif randint < 0:
        print("is negative")