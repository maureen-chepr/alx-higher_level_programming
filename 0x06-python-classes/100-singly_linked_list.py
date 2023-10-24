#!/usr/bin/python3
"""
Singly linked list Module
"""


class Node:
    """
    class Node
    Attributes:
        data (int): data stored in the node
        next_node: pointer to the next node
    """

    def __init__(self, data, next_node=None):
        """initialing class"""

        self.data = data
        self.next_node = None

    @property
    def data(self):
        """attribute getter"""

        return self.__data

    @data.setter
    def data(self, value):
        """attribute setter"""
        if not isinstance(value, int):
            raise TypeError("data must be integer")
        self.__data = value

    @property
    def next_node(self):
        """property getter"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """singly linked list attributes"""

    def __init__(self):
        """initialize class"""

        self.__head = None

    def sorted_insert(self, value):
        """Inserts new Node into the correct sorted position"""

        if self.__head is None:
            self.__head = Node(value, self.__head)
            return
        new_node = Node(value, self.__head)
        self.__head = new_node

    def __str__(self):
        """ creates a list of linked list, sorts, and prints"""
        my_list = []
        runner = self.__head
        while runner is not None:
            my_list.append(runner.data)
            runner = runner.next_node
        my_list.sort()
        final = '\n'.join(str(elem) for elem in my_list)
        return final
