#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """
    Attributes for Square class
    size(int): size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Methods initialized and exception raised"""

        self.size = size
        self.position = position

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

        if self.size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for ind in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print("#" * self.size)

    @property
    def position(self):
        """get postion attribute"""

        return self.__position

    @position.setter
    def position(self, value):
        """
        position setter
        Args:
            value (tuple): position of the square in 2D matrix
        """
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
