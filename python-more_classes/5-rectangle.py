#!/usr/bin/python3
"""
This module defines a Rectangle class with private instance attributes
for width and height, including property getters and setters, public instance.
to calculate the area and perimeter of the rectangle.
and a message printed when an instance of Rectangle is delete.
"""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle wi '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for _ in range(self.__height):
            rect += "#" * self.__width + "\n"
        return rect.rstrip()

    def __repr(self):
        """Returns a string representation of the rectangl eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
