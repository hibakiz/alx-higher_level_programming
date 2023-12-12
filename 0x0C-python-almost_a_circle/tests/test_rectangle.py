#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import json
import inspect



class TestRectangle(unittest.TestCase):

    # Create a Rectangle object with valid arguments and check if the object is created successfully.
    def test_create_rectangle_with_valid_arguments(self):
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)
        self.assertIsNotNone(rectangle.id)

    # Update the attributes of the Rectangle object using valid arguments and check if the attributes are updated successfully.
    def test_update_rectangle_attributes_with_valid_arguments(self):
        rectangle = Rectangle(5, 10)
        rectangle.update(1, 8, 12, 2, 3)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 12)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    # Call the area() method of the Rectangle object and check if it returns the correct area.
    def test_calculate_rectangle_area(self):
        rectangle = Rectangle(5, 10)
        area = rectangle.area()
        self.assertEqual(area, 50)
