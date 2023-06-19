#!/usr/bin/python3
"""Write a function that returns the list of available\
attributes and methods of an objects"""


def lookup(obj):
    """function that returns the list"""
    return dir(obj)
