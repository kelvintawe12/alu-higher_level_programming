#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list[:]
    if idx < 0:
        return temp
    if idx > len(my_list) - 1:
        return temp
    temp[idx] = element
    return temp
