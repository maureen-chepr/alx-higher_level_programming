#!/usr/bin/python3
"""
    class List module
"""


class List:
    """
        superclass:
        class List
    """


class MyList(list):
    """
        subclass:
        class MyList
    """

    def print_sorted(self):
        """
        Prints a sorted List
        """

        print(sorted(self))
