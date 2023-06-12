#!/usr/bin/python3
"""Define a class"""


class Square:
    """Define a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Init Square with size = 0"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        """Init area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Size Value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size of Square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print Square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for j in range(self.__size):
                print(" " * self.position[0], end="")
                for k in range(self.__size):
                    print("{}".format("#"), end="")
                print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
