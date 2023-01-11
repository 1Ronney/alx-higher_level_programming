#!/usr/bin/python3
"""
This is the module that provides the function "is_kind_of_class".
"""


def is_kind_of_class(obj, a_class):
    """
    This is a function that returns True if the object is an instance
    of, or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """
    if issubclass(type(obj), a_class):
        return True
    elif isinstance(obj, a_class):
        return True
    return False
