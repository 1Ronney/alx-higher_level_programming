#!/usr/bin/python3
"""
This is the module that supplies the class LockedClass
"""

class LockedClass:
    """
    class for initializing LockedClass object.
    It prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name
    """
    _slots_ = ['first_name']
