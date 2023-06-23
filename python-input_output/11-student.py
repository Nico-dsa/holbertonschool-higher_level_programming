#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """Represent a Student"""

    def __init__(self, first_name, last_name, age):
        """Init a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dict repres of a Student"""
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """Represent student in Json format"""
        for key, value in json.items():
            setattr(self, key, value)
