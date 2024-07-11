#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
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

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
