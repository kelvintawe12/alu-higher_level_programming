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

# Usage Example
if __name__ == "__main__":
    my_list = MyList([4, 2, 3, 1])
    print("Original list:", my_list)
    print("Sorted list:")
    my_list.print_sorted()
