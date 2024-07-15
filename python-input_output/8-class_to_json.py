#!/usr/bin/python3
"""
Module: 8-class_to_json

This module provides a function that returns the dictionary description with .
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary description of the object.
    """
    return obj.__dict__
