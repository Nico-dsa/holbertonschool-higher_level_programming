#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """Class Mylist"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
