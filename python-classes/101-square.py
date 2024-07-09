#!/usr/bin/python3


class Square:
    """
    Represents a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square with the given size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: Retrieves the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """tuple: Retrieves the position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        Uses the position attribute to determine spaces.
        If size is 0, prints an empty line.
        """
        if self._size == 0:
            print()
            return

        print("\n" * self._position[1], end="")
        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)

    def __str__(self):
        """
        Returns a string representation of the square for printing.

        Returns:
            str: A string representation of the square.
        """
        if self._size == 0:
            return ""

        result = "\n" * self._position[1]
        for _ in range(self._size):
            result += " " * self._position[0] + "#" * self._size + "\n"
        return result.rstrip()

# Example usage
if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
