#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a Rectangle using BaseGeometry"""
    def __init__(self, width, height):
        """Init a new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
