#!/usr/bin/python3
"""Define the base of all other classes"""

from json import dumps, loads
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
