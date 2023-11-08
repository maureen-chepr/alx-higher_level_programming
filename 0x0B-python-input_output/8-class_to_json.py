#!/usr/bin/python3
"""
    dictionary description with simple data structure
    JSON serialization of an object
"""


def class_to_json(obj):
    """
        returns dictionary description with simple data structure
        JSON serialization of an object
    """

    return(obj.__dict__)
