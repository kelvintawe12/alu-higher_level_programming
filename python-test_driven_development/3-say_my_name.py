#!/usr/bin/python3
"""
Module to print a formatted string with first and last names.

This module provides a function to print a string in the format:
"My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Parameters:
    first_name (str): The first name.
    last_name (str): The last name. Default is an empty string.

    Raises:
    TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
