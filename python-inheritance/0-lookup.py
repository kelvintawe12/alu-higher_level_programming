#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the names of the attributes and methods of the object.
    """
    return dir(obj)
