#!/usr/bin/python3
def pow(a, b):
    base = a
    exp = b 
    if a < 0:
        for i in range(0, exp -1):
            base = base * base
    result = 1 / base
    return (result)
    if a > 0:
        for i in range(0, exp - 1):
            base = base * base
    result = base
    return (result) 
