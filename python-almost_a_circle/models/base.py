#!/usr/bin/python3
"""Define the base of all other classes"""


class Base:
    """Base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
