#!/usr/bin/python3
"""
Module: 2-append_write

This module provides a function to append a string to a text file and
return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the
    number of characters added.

    Args:
        filename (str): The name of the file to append to.
                        Defaults to an empty string.
        text (str): The string to append to the file. Defaults to an
                    empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        nb_characters_added = append_write(sys.argv[1], sys.argv[2])
        print(nb_characters_added)
    else:
        print("Usage: ./2-main.py <filename> <text>")
