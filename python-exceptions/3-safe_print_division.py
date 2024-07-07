#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result:", result)
        return result

# Example usage:
a = 10
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 10
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
