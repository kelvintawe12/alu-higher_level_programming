#!/usr/bin/python3

def pow(a, b):
    """
    Returns the value of a^b.
    """
    result = 1
    for _ in range(abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    return result

# Example usage:
print(pow(2, 2)
print(pow(98, 2))
print(pow(98, 0))   
print(pow(100, -2)) 
print(pow(-4, 5))
