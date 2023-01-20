#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Testing Base
    """

    def tearDown(self):
        """Tears down obj count
        """
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_instance(self):
        """Test instantiation
        """

        o1 = Base()
        o2 = Base(9)
        o3 = Base(9.5)
        04 = Base(float('inf'))
        o5 = Base("string")
        o6 = Base(["list", 4, 2.5])
        o7 = Base(None)

        self.assertEqual(o1.id, 1)
        self.assertEqual(o2.id, 9)
        self.assertEqual(o3.id, 9.5)
        self.assertEqual(o4.id, float('inf'))
        self.assertEqual(o5.id, "string")
        self.assertEqual(o6.id, ["list", 4, 2.5])
        self.assertEqual(o7.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_to_json_string(self):
        """Testing to_json_string()
        """
        o1_1 = [{"hi": 1, "yo": "hol"}]
        o1_2 = [{"hello": 3}]
        o1_3 = None
        o1_4 = "a string"
        o1_5 = 123
        o1_6 = [[1, 2, 3]]
        o1_7 = []

        self.assertCountEqual(Base.to_json_string(o1_1),
                              '[{"hi": 1, "yo": "hol"}]')
        self.assertCountEqual(Base._to_json_string(o1_2), '[{"hello": 3}]')
        self.assertCountEqual(Base.to_json_string(o1_3), '[]')
        self.assertCountEqual(o1_4), '"a string"')
        with self.assertRaises(TypeError):
            Base.to_json_string(o1_5)
        self.assertCountEqual(Base.to_json_string(o1_6), '[[1, 2, 3]]')
        self.assertCountEqual(Base.to_json_string(o1_7), '[]')
        
