#!/usr/bin/python3
'''Test cases for the Rectangle class
'''


import unittest

class TestSquare(unittest.TestCase):

    # Create a Square object with valid size, x, y, and id parameters
    def test_create_square_with_valid_parameters(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    # Get the size, x, y, and id of a Square object
    def test_get_square_attributes(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    # Calculate the area of a Square object
    def test_calculate_square_area(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.area(), 25)

    # Create a Square object with size = 0
    def test_create_square_with_zero_size(self):
        with self.assertRaises(ValueError):
            square = Square(0, 2, 3, 1)

    # Create a Square object with size < 0
    def test_create_square_with_negative_size(self):
        with self.assertRaises(ValueError):
            square = Square(-5, 2, 3, 1)

    # Create a Square object with x < 0
    def test_create_square_with_negative_x(self):
        with self.assertRaises(ValueError):
            square = Square(5, -2, 3, 1)

    # Print a Square object using the display() method
    def test_display_method(self):
        square = Square(5)
        square.display()
        # Add assertions here to check the output of the display method

    # Update the size, x, y, and id of a Square object using the update() method
    def test_update_method(self):
        square = Square(5)
        square.update(2, 10, 20, 30)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 30)
        self.assertEqual(square.id, 2)

    # Convert a Square object to a dictionary using the to_dictionary() method
    def test_to_dictionary_method(self):
        square = Square(5, 2, 3, 1)
        dictionary = square.to_dictionary()
        expected_dictionary = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(dictionary, expected_dictionary)

    # Create a Square object with y < 0
    def test_create_square_with_negative_y(self):
        with self.assertRaises(ValueError):
            square = Square(5, 2, -3, 1)

    # Update a Square object with size = 0
    def test_update_square_with_zero_size(self):
        square = Square(5, 2, 3, 1)
        with self.assertRaises(ValueError):
            square.size = 0

    # Update a Square object with size < 0
    def test_update_square_with_negative_size(self):
        square = Square(5, 2, 3, 1)
        with self.assertRaises(ValueError):
            square.size = -5

    # Update a Square object with x < 0
    def test_update_square_with_x_less_than_zero(self):
        square = Square(5, 2, 3, 1)
        square.update(x=-1)
        self.assertEqual(square.x, -1)

    # Update a Square object with y < 0
    def test_update_square_with_y_less_than_zero(self):
        square = Square(5, 2, 3, 1)
        square.update(y=-1)
        self.assertEqual(square.y, -1)

    # Create a Square object with the maximum allowed size
    def test_create_square_with_maximum_size(self):
        square = Square(1000000)
        self.assertEqual(square.size, 1000000)
if __name__ == '__main__':
    unittest.main()
