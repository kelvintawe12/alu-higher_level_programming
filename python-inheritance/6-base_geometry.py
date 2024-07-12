#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
"""


class BaseGeometry:
    """
    A class representing the base geometry.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implement.

        Raises:
            Exception: Always raises an Exception with the message "area()..".
        """
        raise Exception("area() is not implemented")
