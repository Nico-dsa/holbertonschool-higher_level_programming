#!/usr/bin/python3
"""Write an empty class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry"""
    def area(self):
        """Is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """That validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
