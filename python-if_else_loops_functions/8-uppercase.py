#!/usr/bin/python3

def uppercase(s):
    """
    Prints the input string in uppercase followed by a new line.
    """
    for char in s:
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - 32)), end='')
        else:
            print("{}".format(char), end='')
    print()

# Example usage
uppercase("best")  # Output: BEST
uppercase("Best School 98 Battery street")
