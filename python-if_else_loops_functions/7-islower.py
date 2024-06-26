#!/usr/bin/python3

def islower(c):
    """
    Returns True if c is lowercase, False otherwise.
    """
    return ord('a') <= ord(c) <= ord('z')

# Example usage
print(islower("a"))  # True
print(islower("H"))  # False
print(islower("A"))  # False
print(islower("3"))  # False
print(islower("g"))  # True
