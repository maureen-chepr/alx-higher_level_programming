#!/usr/bin/python3
"""
    is_same_class function
"""


def is_same_class(obj, a_class):
    """
    check if object is exactly an instance
    of the specified class
    Return: True or False
    """
    return type(obj) is a_class
