#!/usr/bin/python3
"""A subclass of list that provides an additional method to print the list"""


class MyList(list):
    """
    A subclass of list that provides an additional method to print the list
    in sorted order.
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending order.
        Assumes all elements are of type int.
        """
        print(sorted(self))

