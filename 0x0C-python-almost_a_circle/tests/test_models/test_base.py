#!/usr/bin/python3
""" Test module for the Base Class """
import unittest
from models.base import Base


class testBaseClass(unittest.TestCase):
    """the class the hold each test case 
    for the inputs of Base class functions"""

    def check_id_value(self):  # init function
        self.assertRaises(ValueError, Base(), -2)  # negative

    def check_id_type(self):  # init function
        self.assertRaises(TypeError, Base, "hi")
        self.assertRaises(TypeError, Base, "a")
        self.assertRaises(TypeError, Base, "7")
        self.assertRaises(TypeError, Base(), 1.5)

    def test_to_json_string(self):
        self.assertRaises(TypeError, Base.to_json_string(), 1)
        self.assertRaises(TypeError, Base.to_json_string(), {"id: 8"})
        self.assertRaises(TypeError, Base.to_json_string(), (7, "l"))
        self.assertRaises(TypeError, Base.to_json_string(), 1.5)

    def test_to_json_string2(self):
        # Test case for non-list input
        with self.assertRaises(TypeError):
            Base.to_json_string("not_a_list")

        # Test case for empty list input
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test case for list of dictionaries input
        input_list = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        expected_output = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(Base.to_json_string(input_list), expected_output)

    def test_save_to_file(self):
        self.assertRaises(TypeError, Base.save_to_file(), 1)
        self.assertRaises(TypeError, Base.save_to_file(), {"id: 8"})
        self.assertRaises(TypeError, Base.save_to_file(), (7, "l"))
        self.assertRaises(TypeError, Base.save_to_file(), 1.5)

    def test_from_json_string(self):
        self.assertRaises(TypeError, Base.from_json_string(), 1)
        self.assertRaises(TypeError, Base.from_json_string(), {"id: 8"})
        self.assertRaises(TypeError, Base.from_json_string(), (7, "l"))
        self.assertRaises(TypeError, Base.from_json_string(), 1.5)

    def test_create(self):
        self.assertRaises(TypeError, Base.create(), 1)
        self.assertRaises(TypeError, Base.create(), ["id", 8])
        self.assertRaises(TypeError, Base.create(), (7, "l"))
        self.assertRaises(TypeError, Base.create(), 1.5)
