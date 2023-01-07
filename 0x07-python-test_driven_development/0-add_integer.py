#!/usr/bin/python3
"""
This is the modue that supplies the function add_integer
"""

def add_integer(a, b=98):
    """
    adds two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
