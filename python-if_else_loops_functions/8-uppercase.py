#!/usr/bin/python3
def uppercase(str):
    uprstr = ""
    for a in str:
        if ord(a) >= ord('a') and ord(a) <= ord('z'):
            uprstr += chr(ord(i) - 32)
        else:
            uprstr += i
    print('{}'.format(uprstr))
