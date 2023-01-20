!/usr/bin/python3
"""Test Base Module"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    
    """TestBase Class"""
    
    def setUp(self):
        
        pass
    

    
    def tearDown(self):
        
        Base._Base__nb_objects = 0
        
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.isfile("Square.json"):
            os.remove("Square.json")
        if os.path.isfile("Base.json"):
            os.remove("Base.json")