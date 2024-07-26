#!/usr/bin/python3
"""
Module for adding two integers.
This module provides a function to add two numbers,
ensuring that both inputs are integers or floats,
and handles type errors appropriately.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.
    Parameters:
    a (int, float): The first number.
    b (int, float, optional): The second number, defaults to 98.
    Returns:
    int: The sum of a and b, cast to an integer.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
