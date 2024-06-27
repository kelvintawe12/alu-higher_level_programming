#!/usr/bin/python3
def uppercase(str):
    for iterator in str:
        temp = iterator
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(iterator) - 32)
        print("{}".format(temp), end='')
    print()
