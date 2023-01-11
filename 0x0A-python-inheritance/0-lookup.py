#!/usr/bin/python3

"""
This is a module that supplies the function "lookup".
"""


def lookup(obj):
    """
    This function returns a list of the attributes and methods in an object
    """
    return dir(obj)
