#!/usr/bin/python3
"""
This module defines a function to check if an object is an instance.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if obj is an instance of a class that inherite False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
