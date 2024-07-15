#!/usr/bin/python3
"""
Module: 0-read_file

This module provides a function to read a text file and print its
contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
                        Defaults to an empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        read_file(sys.argv[1])
    else:
        print("Usage: ./0-main.py <filename>")
