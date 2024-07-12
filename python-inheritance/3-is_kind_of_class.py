#!/usr/bin/python3
"""
This module defines a function to check if an object is an instance of,
or if the object is an instance of a class that inherited from, hjj.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object .
    of a class that inherited from, the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of or inherits from a_class, otherwise.
    """
    return isinstance(obj, a_class)
