#!/usr/bin/python3
"""
Module to print a text with 2 new lines after each of the characters
., ? and :.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    ., ? and :.

    Parameters:
    text (str): The text to format.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = {'.', '?', ':'}
    result = []
    skip_space = False

    for char in text:
        if char in special_chars:
            result.append(char)
            result.append('\n')
            result.append('\n')
            skip_space = True
        elif char == ' ':
            if skip_space:
                continue
            result.append(char)
        else:
            result.append(char)
            skip_space = False

    print(''.join(result).strip())
