#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from int with inverted.
"""


class MyInt(int):
    """
    A class representing an integer with inverted equality operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.
        """
        return super().__eq__(other)
