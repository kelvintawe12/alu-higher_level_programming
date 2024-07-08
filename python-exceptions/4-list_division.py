#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError
            value1 = my_list_1[i]
            value2 = my_list_2[i]
            if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
                raise TypeError
            if value2 == 0:
                raise ZeroDivisionError
            result.append(value1 / value2)
        except TypeError:
            print("wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result

