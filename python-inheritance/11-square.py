#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

class Rectangle:
    """
    A class to represent a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """
        Validate that a given value is a positive integer.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def __str__(self):
        """
        Return the string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """
    A class to represent a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize the square with size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())

