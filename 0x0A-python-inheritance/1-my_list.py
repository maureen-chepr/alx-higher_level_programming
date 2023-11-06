#!/usr/bin/python3
"""
    class List module
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
