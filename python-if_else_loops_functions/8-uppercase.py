#!/usr/bin/python3
def uppercase(str):
    uprstr = ""
    for a in str:
        if ord(a) >= ord('a') and ord(a) <= ord('z'):
            upstr += chr(ord(i) - 32)
        else:
            upstr += i
    print('{}'.format(uprstr))
