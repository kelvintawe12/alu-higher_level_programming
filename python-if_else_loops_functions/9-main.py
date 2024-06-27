#!/usr/bin/env python3

def custom_concatenate_last_digits(*args):
    string = ''
    for each in args:
        string += str(each)
    return int(string)

result = custom_concatenate_last_digits(98, 0, -1024)
print(result)
