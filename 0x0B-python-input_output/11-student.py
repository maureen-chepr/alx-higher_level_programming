#!/usr/bin/python3
"""
    class Student module
"""


class Student():
    """
        class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
            initialization of class student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves a dictionary representation
            of a Student instance
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict_

    def reload_from_json(self, json):
        """
            replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)_
