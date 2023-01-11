#!/usr/bin/python3
"""
This module provides the class "Square".
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from the base class "Rectangle"
    """
    def __init__(self, size):
        super().__init__(size, size)
