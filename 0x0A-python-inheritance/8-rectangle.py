#!/usr/bin/python3
"""
    Rectangle module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
            Initialization of class rectangle from BaseGeometry
        """

        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
