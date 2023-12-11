#!/usr/bin/python3
'''Test cases for the Rectangle class
'''

import unittest


class TestRectangle:

    # Creating a rectangle with valid width, height, x, y, and id.
    def test_create_rectangle_with_valid_values(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        assert rectangle.width == 5
        assert rectangle.height == 10
        assert rectangle.x == 2
        assert rectangle.y == 3
        assert rectangle.id == 1

    # Updating a rectangle's width, height, x, y, and id with valid values.
    def test_update_rectangle_with_valid_values(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle.update(2, 8, 4, 6, 1)
        assert rectangle.width == 8
        assert rectangle.height == 4
        assert rectangle.x == 6
        assert rectangle.y == 1
        assert rectangle.id == 2

    # Getting the area of a rectangle.
    def test_get_rectangle_area(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        assert rectangle.area() == 50

    # Creating a rectangle with width or height equal to 0.
    def test_create_rectangle_with_zero_width_or_height(self):
        with pytest.raises(ValueError):
            rectangle = Rectangle(0, 10, 2, 3, 1)
        with pytest.raises(ValueError):
            rectangle = Rectangle(5, 0, 2, 3, 1)

    # Creating a rectangle with negative x or y values.
    def test_create_rectangle_with_negative_x_or_y(self):
        with pytest.raises(ValueError):
            rectangle = Rectangle(5, 10, -2, 3, 1)
        with pytest.raises(ValueError):
            rectangle = Rectangle(5, 10, 2, -3, 1)

    # Creating a rectangle with non-integer width, height, x, or y values.
    def test_create_rectangle_with_non_integer_values(self):
        with pytest.raises(TypeError):
            rectangle = Rectangle(5.5, 10, 2, 3, 1)
        with pytest.raises(TypeError):
            rectangle = Rectangle(5, 10.5, 2, 3, 1)
        with pytest.raises(TypeError):
            rectangle = Rectangle(5, 10, 2.5, 3, 1)
        with pytest.raises(TypeError):
            rectangle = Rectangle(5, 10, 2, 3.5, 1)

    # Converting a rectangle to a dictionary.
    def test_convert_to_dictionary(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        dictionary = rectangle.to_dictionary()
        assert isinstance(dictionary, dict)
        assert dictionary['id'] == 1
        assert dictionary['width'] == 5
        assert dictionary['height'] == 10
        assert dictionary['x'] == 2
        assert dictionary['y'] == 3

    # Displaying a rectangle using the display method.
    def test_display_rectangle(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle.display()
            expected_output = "          ##########\n          ##########\n          ##########\n          ##########\n          ##########\n          ##########\n          ##########\n          ##########\n          ##########\n          ##########\n"
            self.assertEqual(fake_out.getvalue(), expected_output)

    # Updating a rectangle's width or height with a non-integer value.
    def test_update_with_non_integer_value(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        with self.assertRaises(TypeError):
            rectangle.width = "5"
        with self.assertRaises(TypeError):
            rectangle.height = "10"

    # Updating a rectangle's x or y with a negative value.
    def test_update_rectangle_with_negative_x_or_y(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle.x = -1
        assert rectangle.x == -1
        rectangle.y = -2
        assert rectangle.y == -2

    # Creating a rectangle with the minimum valid values for width, height, x, y, and id.
    def test_create_rectangle_with_minimum_valid_values(self):
        rectangle = Rectangle(1, 1)
        assert rectangle.width == 1
        assert rectangle.height == 1
        assert rectangle.x == 0
        assert rectangle.y == 0
        assert rectangle.id is not None

    # Creating a rectangle with the maximum valid values for width, height, x, y, and id.
    def test_create_rectangle_with_maximum_valid_values(self):
        rectangle = Rectangle(1000000, 1000000, 999999, 999999, 999999)
        assert rectangle.width == 1000000
        assert rectangle.height == 1000000
        assert rectangle.x == 999999
        assert rectangle.y == 999999
        assert rectangle.id == 999999

if __name__ == '__main__':
    unittest.main()
