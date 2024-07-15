#!/usr/bin/python3
"""
Module: 6-load_from_json_file

This module provides a function to create an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            obj = load_from_json_file(filename)
            print(obj)
            print(type(obj))
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
    else:
        print("Usage: ./6-main.py <filename>")
