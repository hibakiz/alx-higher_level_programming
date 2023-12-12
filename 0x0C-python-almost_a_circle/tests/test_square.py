#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):

    # Create a square with valid arguments, and check if the attributes are set correctly.
    def test_valid_arguments(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 8)

    # Update the square attributes using the update method, and check if the attributes are updated correctly.
    def test_update_attributes(self):
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 10)

    # Call the to_dictionary method, and check if the returned dictionary is correct.
    def test_to_dictionary(self):
        s = Square(5)
        expected_dict = {'id': 6, 'size': 5, 'x': 0, 'y': 0}
        self.assertEqual(s.to_dictionary(), expected_dict)

    # Create a square with size 0, and check if a ValueError is raised.
    def test_size_zero(self):
        with self.assertRaises(ValueError):
            s = Square(0)

    # Create a square with negative size, and check if a ValueError is raised.
    def test_negative_size(self):
        with self.assertRaises(ValueError):
            s = Square(-5)

    # Create a square with size that is not an integer, and check if a TypeError is raised.
    def test_non_integer_size(self):
        with self.assertRaises(TypeError):
            s = Square("5")
