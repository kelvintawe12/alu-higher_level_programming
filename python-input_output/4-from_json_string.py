#!/usr/bin/python3
"""
Module: 4-from_json_string

This module provides a function to return a Python object represented
by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to a Python object.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        json_str = sys.argv[1]
        obj = from_json_string(json_str)
        print(obj)
        print(type(obj))
    else:
        print("Usage: ./4-main.py '<json_string>'")
