#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list, \
and then save them to a file"""
import sys


save = __import__('5-save_to_json_file.py').save_to_json_file
load = __import__('6-load_from_json_file.py').load_from_json_file


def lists(argument):
    """add argument"""
    try:
        value = load("add_item.json")
    except FileNotFoundError:
        value = []

    value += argument
    save(value, "add_item.json")


argument = sys.argv[1:]
lists(argument)
