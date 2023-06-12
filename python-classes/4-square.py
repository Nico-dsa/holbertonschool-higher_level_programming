#!/usr/bin/python3
"""Define a class"""


class Square:
    """Define a Square"""
    def __init__(self, size=0):
        """Init Square with size = 0"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

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
