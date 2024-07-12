#!/usr/bin/python3
"""
This module defines a function add_attribute to add a new attribute.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute should be added.
        attribute (str): The name of the attribute to add.
        value: The value of the attribute to set.

    Raises:
        TypeError: If the object does not allow new attributes to be added.
    """
    if hasattr(obj, '__slots__'):
        if attribute not in obj.__slots__:
            raise TypeError("can't add new attribute")
    elif not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
