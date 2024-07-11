#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
