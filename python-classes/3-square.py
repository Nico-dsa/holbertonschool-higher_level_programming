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
        """Init Square with area"""
        return self.__size * self.__size