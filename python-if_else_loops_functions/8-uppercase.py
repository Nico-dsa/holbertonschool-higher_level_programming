#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            j = ord(i)
            i = chr(j - 32)
        print("{}".format(i), end='')
    print()
