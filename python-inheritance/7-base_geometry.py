#!/usr/bin/python3
"""
This module defines a class BaseGeometry with methods for geometric operations.
"""

class BaseGeometry:
    """
    A class representing the base geometry with geometric operations.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the given value is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
