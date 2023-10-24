#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """
    Attributes for Square class
    size(int): size of square
    """

    def __init__(self, size=0):
        """Methods initialized and exception raised"""

        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        current square area
        Return:
             area
        """
        area = self.__size ** 2
        return area

    @property
    def size(self):
        """
        size getter
        Return:
             area
        """

        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""

        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.__size == 0:
            print()
        else:
            for ind in range(0, self.size):
                print("#" * self.size)
