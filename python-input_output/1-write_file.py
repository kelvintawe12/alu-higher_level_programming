#!/usr/bin/python3
"""
Module: 1-write_file

This module provides a function to write a string to a text file and
return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of
    characters written.

    Args:
        filename (str): The name of the file to write to.
                        Defaults to an empty string.
        text (str): The string to write to the file. Defaults to an
                    empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        nb_characters = write_file(sys.argv[1], sys.argv[2])
        print(nb_characters)
    else:
        print("Usage: ./1-main.py <filename> <text>")
