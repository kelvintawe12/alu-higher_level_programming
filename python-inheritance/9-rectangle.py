#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """
        Validate that a given value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def __str__(self):
        """
        Return the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
