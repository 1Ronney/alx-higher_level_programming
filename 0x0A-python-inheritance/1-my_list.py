#!/usr/bin/python3
"""
This is the module that supplies the class "my_list"
"""


class MyList(list):

    """
    This is an object that inherits the list built-in object.
    The object has a print_sorted instance method that prints
    the contents of the list in ascending order.
    """
    def print_sorted(self):
        new = self.copy()
        new.sort()
        print(new)
