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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file."""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary()
                                         for obj in list_objs])

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string."""
        if json_string is None or json_string == []:
            return "[]"
        return json.loads(json_string)