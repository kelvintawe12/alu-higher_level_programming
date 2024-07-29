#!/usr/bin/python3
""" python text for indentations"""


def text_indentation(text):
    """ defining the text indentation.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
