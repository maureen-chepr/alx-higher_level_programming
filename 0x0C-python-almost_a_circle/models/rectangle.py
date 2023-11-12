#!/usr/bin/python3
"""
    models/rectangle.py module
"""
from models.base import Base


class Rectangle(Base):
    """
        class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initialization of Rectangle class
            Args:
            width
            height
            x
            y
            id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            returns the area value of Rectangle instance
        """

        return self.__width * self.__height

    def display(self):
        """
            prints in stdout the Rectangle instance
            with the character #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """
            returns formatted str
        """

        return (f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def to_dictionary(self):
        """
            returns the dictionary representation of a Rectangle
        """
        return{
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

    def update(self, *args, **kwargs):
        """
            assigns an argument to each attribute
        """
        if args:
            super().update(*args)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
