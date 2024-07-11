#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

# Import the Rectangle class from 9-rectangle.py
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class to represent a square, inheriting from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initialize the square with size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the string representation of the square as a rectangle.

        Returns:
            str: The string representation of the square as a rectangle.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
