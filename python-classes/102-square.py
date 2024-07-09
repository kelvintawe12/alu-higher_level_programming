#!/usr/bin/python3


class Square:
    """
    Represents a square.

    Attributes:
        size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square with the given size.

        Args:
            size (float or int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """float or int: Retrieves the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self._size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on their area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on their area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square is less than another based on their area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square is less than or equal to another based on their area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square is greater than another based on their area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square is greater than or equal to another based on their area."""
        return self.area() >= other.area()


# Example usage
if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
