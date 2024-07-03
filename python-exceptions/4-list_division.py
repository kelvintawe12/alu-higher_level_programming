#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            value1 = my_list_1[i] if i < len(my_list_1) else 0
            value2 = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
                print("wrong type")
                result.append(0)
            elif value2 == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(value1 / value2)
        except IndexError:
            print("out of range")
            result.append(0)

    return result
