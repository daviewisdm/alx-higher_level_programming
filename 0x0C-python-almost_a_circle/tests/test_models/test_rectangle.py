#!/usr/bin/python3
""" Test module for the Base Class """
import unittest
from models.rectangle import Rectangle


class testRectangleeClass(unittest.TestCase):
    """the class the hold each test case for the inputs of Rectangle class functions"""

    def _test_init(self):
        self.assertRaises(TypeError, Rectangle(), 8, 0, "l", "hi", "hi")
        self.assertRaises(TypeError, Rectangle(), "a", "7", 7, 9, 10)
        self.assertRaises(TypeError, Rectangle(), 7, 6, "hi", 8, 0)
        self.assertRaises(TypeError, Rectangle(), 1.5, "oop")

    def test_update_with_positional_arguments(self):
        # Test updating attributes using positional arguments
        obj = Rectangle(attr1=1, attr2=2)
        obj.update(3, 4)
        self.assertEqual(obj.attr1, 3)
        self.assertEqual(obj.attr2, 4)

    def test_update_with_keyword_arguments(self):
        # Test updating attributes using keyword arguments
        obj = Rectangle(attr1=1, attr2=2)
        obj.update(attr1=3, attr2=4)
        self.assertEqual(obj.attr1, 3)
        self.assertEqual(obj.attr2, 4)

    def test_update_with_mixed_arguments(self):
        # Test updating attributes using a mix of positional and keyword arguments
        obj = Rectangle(attr1=1, attr2=2)
        obj.update(3, attr2=4)  # Update attr1 with positional, attr2 with keyword
        self.assertEqual(obj.attr1, 3)
        self.assertEqual(obj.attr2, 4)

    def test_update_with_no_arguments(self):
        # Test update method with no arguments (should not modify attributes)
        obj = Rectangle(attr1=1, attr2=2)
        obj.update()
        self.assertEqual(obj.attr1, 1)  # unchanged
        self.assertEqual(obj.attr2, 2)  # unchanged

    def setUp(self):
        self.rectangle = Rectangle(4, 6, 2, 3, 1)

    def test_str(self):
        self.assertEqual(str(self.rectangle), "[Rectangle] (1) 2/3 - 4/6")

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 24)

    def test_display(self):
        expected_output = "\n\n  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output
        self.rectangle.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_update(self):
        self.rectangle.update(10)
        self.assertEqual(self.rectangle.width, 10)
        self.assertEqual(self.rectangle.height, 6)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 3)
        self.assertEqual(self.rectangle.id, 1)

        self.rectangle.update(20, 4, 5, 6)
        self.assertEqual(self.rectangle.width, 20)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 5)
        self.assertEqual(self.rectangle.y, 6)
        self.assertEqual(self.rectangle.id, 1)

        self.rectangle.update(y=50, width=30)
        self.assertEqual(self.rectangle.width, 30)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 5)
        self.assertEqual(self.rectangle.y, 50)
        self.assertEqual(self.rectangle.id, 1)

    def test_to_dictionary(self):
        expected_dict = {"x": 2, "y": 3, "id": 1, "height": 6, "width": 4}
        self.assertDictEqual(self.rectangle.to_dictionary(), expected_dict)
