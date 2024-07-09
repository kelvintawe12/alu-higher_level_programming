#!/usr/bin/python3


class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node with the given data and next node.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the linked list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: Retrieves the data stored in the node."""
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Node: Retrieves the next node in the linked list."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the entire linked list.

        Returns:
            str: A string representation of the linked list, with each node's data on a new line.
        """
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the correct sorted position in the list.

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node


# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(3)
    sll.sorted_insert(1)
    sll.sorted_insert(7)
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(4)
    print(sll)
