#!/usr/bin/python3
""" Test module for the Base Class """
import unittest
from models.square import Square


class testSquareeClass(unittest.TestCase):
    """the class the hold each test case for the inputs of Square class functions"""

    def _test_init(self):
        self.assertRaises(TypeError, Square(), 8, 0, "l", "hi", "hi")
        self.assertRaises(TypeError, Square(), "a", "7", 7, 9, 10)
        self.assertRaises(TypeError, Square(), 7, 6, "hi", 8, 0)
        self.assertRaises(TypeError, Square(), 1.5, "oop")

    def test_update_with_positional_arguments(self):
        # Test updating attributes using positional arguments
        obj = Square(attr1=1, attr2=2)
        obj.update(3, 4)
        self.assertEqual(obj.attr1, 3)
        self.assertEqual(obj.attr2, 4)

    def test_update_with_keyword_arguments(self):
        # Test updating attributes using keyword arguments
        obj = Square(attr1=1, attr2=2)
        obj.update(attr1=3, attr2=4)
        self.assertEqual(obj.attr1, 3)
        self.assertEqual(obj.attr2, 4)

    def test_update_with_mixed_arguments(self):
        # Test updating attributes using a mix of positional and keyword arguments
        obj = Square(attr1=1, attr2=2)
        obj.update(3, attr2=4)
        self.assertEqual(obj.attr1, 3)
        self.assertEqual(obj.attr2, 4)

    def test_update_with_no_arguments(self):
        # Test update method with no arguments (should not modify attributes)
        obj = Square(attr1=1, attr2=2)
        obj.update()
        self.assertEqual(obj.attr1, 1)  # unchanged
        self.assertEqual(obj.attr2, 2)  # unchanged

    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_str(self):
        self.assertEqual(str(self.square), "[Square] (1) 2/3 - 5")

    def test_size(self):
        self.assertEqual(self.square.size, 5)

    def test_size_setter(self):
        self.square.size = 10
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.width, 10)
        self.assertEqual(self.square.height, 10)

    def test_update(self):
        self.square.update(10)
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

        self.square.update(20, 4, 5, 6)
        self.assertEqual(self.square.size, 20)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 5)
        self.assertEqual(self.square.id, 6)

        self.square.update(y=50, size=30)
        self.assertEqual(self.square.size, 30)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 50)
        self.assertEqual(self.square.id, 6)

    def test_to_dictionary(self):
        expected_dict = {"id": 1, "size": 5, "x": 2, "y": 3}
        self.assertDictEqual(self.square.to_dictionary(), expected_dict)
