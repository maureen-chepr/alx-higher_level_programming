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
        if not type(value) is int:
            raise TypeError("data must be integer")
        else:
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

    def __str__(self):
        result = ""
        temp = self.__head
        while temp is not None:
            result += str(self.data)
            result += '\n'
            temp = temp.__next_node
        return result

    def sorted_insert(self, value):
        """Inserts new Node into the correct sorted position"""

        if self.__head is None:
            self.__head = Node(value)
        else:
            new_node = Node(value)
            temp = self.__head
            while temp is not None:
                if temp.__next_node is None:
                    temp.__next_node = new_node
                    new_node.__next_node = None
                if new_node.__data < temp.__next_node.__data:
                    new_node.__next_node = temp.__next_node
                    temp.__next_node = new_node
                temp = temp.__next_node
