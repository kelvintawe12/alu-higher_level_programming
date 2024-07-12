#!/usr/bin/python3


class MyList(list):
    """ this is a simple My-list class as you can see that it officially."""
    def print_sorted(self):
        """Prints the list, but sorted  sorted prints in alphabetical order(ascending sort)"""
        print(sorted(self))
