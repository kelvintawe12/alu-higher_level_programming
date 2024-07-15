#!/usr/bin/python3
"""
Module: 5-save_to_json_file

This module provides a function to write an object to a text file using
a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized to JSON and written to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        obj = eval(sys.argv[1])
        filename = sys.argv[2]
        save_to_json_file(obj, filename)
    else:
        print("Usage: ./5-main.py '<object>' <filename>")
