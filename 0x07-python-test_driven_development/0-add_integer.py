#!/usr/bin/python3

"""
function that adds 2 integers
Args: a, b
a and b must be integers,otherwise raise a TypeError
"""


def add_integer(a, b=98):
    """
    result = a + b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
