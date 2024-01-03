#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            char = chr(ord(i) - 32)
        else:
            char = i
        print("{:s}".format(char), end="")
    print()
