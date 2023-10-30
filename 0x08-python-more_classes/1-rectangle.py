#!/usr/bin/python3

"""
class Rectangle module
"""


class Rectangle:
    """
    class Rectangle
    Private instance attribute:
    (int)width:
    (int)height:
    """

    def __init__(self, width=0, height=0):
        """
        methods initialized
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        returns:
        width of the Rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
        value: the value to be set
        raises:
        TypeError:width must be an integer
        ValueError:width must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
        value: the value to be set
        raises:
        TypeError:height must be an integer
        ValueError:height must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
