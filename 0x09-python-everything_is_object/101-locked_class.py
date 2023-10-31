#!/usr/bin/python3

"""
    locked class module
"""


class LockedClass:
    """
        class LockedClass with no class or object attribute
        it prevents the user from dynamically creating new instance attributes
    """

    __slots__ = "first_name"
