#!/usr/bin/python3
"""
Module: 3-to_json_string

This module provides a function to return the JSON representation of
an object.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        obj = eval(sys.argv[1])
        json_string = to_json_string(obj)
        print(json_string)
        print(type(json_string))
    else:
        print("Usage: ./3-main.py '<object>'")
