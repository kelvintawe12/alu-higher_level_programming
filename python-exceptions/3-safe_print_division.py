#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result:", result)
        return result
a = 10
b = 0
result = safe_print_division(a, b)
if result is not None:
    print("Formatted result: {:.2f}".format(result))
