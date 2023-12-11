#!/usr/bin/python3
'''Test cases for the base class
'''


import unittest
import inspect
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_create_instance_with_no_arguments(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_multiple_instances_without_id(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_to_json_string_with_list_of_dictionaries(self):
        base1 = Base(1)
        base2 = Base(2)
        base3 = Base(3)
        list_dictionaries = [base1.to_dictionary(),
                             base2.to_dictionary(), base3.to_dictionary()]
        json_string = Base.to_json_string(list_dictionaries)
        expected_json_string = '[{"id": 1}, {"id": 2}, {"id": 3}]'
        self.assertEqual(json_string, expected_json_string)

    def test_to_json_string_with_empty_list(self):
        list_dictionaries = []
        json_string = Base.to_json_string(list_dictionaries)
        expected_json_string = '[]'
        self.assertEqual(json_string, expected_json_string)

    def test_save_to_file_with_none_argument(self):
        Base.save_to_file(None)
        filename = 'Base.json'
        with open(filename, 'r') as f:
            json_string = f.read()
            expected_json_string = '[]'
            self.assertEqual(json_string, expected_json_string)
        os.remove(filename)

    def test_from_json_string_with_empty_string(self):
        json_string = ''
        list_dictionaries = Base.from_json_string(json_string)
        expected_list_dictionaries = []
        self.assertEqual(list_dictionaries, expected_list_dictionaries)

    def test_save_to_file(self):
        # Create a list of objects
        objs = [Base(1), Base(2), Base(3)]

        # Call the save_to_file method
        Base.save_to_file(objs)

        # Check if the file exists
        self.assertTrue(os.path.exists("Base.json"))

        # Read the contents of the file
        with open("Base.json", "r") as f:
            contents = f.read()

        expected = '[{"id": 1}, {"id": 2}, {"id": 3}]'
        self.assertEqual(contents, expected)

        # Delete the file
        os.remove("Base.json")

    def test_from_json_string(self):
        # Create a JSON string
        json_string = '[{"id": 1}, {"id": 2}, {"id": 3}]'

        # Call the from_json_string method
        result = Base.from_json_string(json_string)

        # Check if the result is a list
        self.assertIsInstance(result, list)

        # Check if each element in the list is a dictionary
        for element in result:
            self.assertIsInstance(element, dict)

        # Check if the dictionaries match the expected values
        expected = [{"id": 1}, {"id": 2}, {"id": 3}]
        self.assertEqual(result, expected)

    def test_create(self):
        # Create a dictionary
        dictionary = {"id": 1, "width": 10, "height": 20, "x": 5, "y": 5}

        # Call the create method
        result = Base.create(**dictionary)

        # Check if the result is an instance of the class
        self.assertIsInstance(result, Base)

        # Check if the attributes match the expected values
        self.assertEqual(result.id, 1)
        self.assertEqual(result.width, 10)
        self.assertEqual(result.height, 20)
        self.assertEqual(result.x, 5)
        self.assertEqual(result.y, 5)

    def test_load_from_file(self):
        # Create instances of the class
        obj1 = Base(1)
        obj2 = Base(2)
        obj3 = Base(3)

        # Save the instances to a JSON file
        Base.save_to_file([obj1, obj2, obj3])

        # Load the instances from the JSON file
        loaded_objs = Base.load_from_file()

        # Check if the loaded objects are instances of the class
        for obj in loaded_objs:
            self.assertIsInstance(obj, Base)

    def test_save_to_file_csv(self):
        # Create instances of the class
        obj1 = Base(1)
        obj2 = Base(2)
        obj3 = Base(3)

        # Save the instances to a CSV file
        Base.save_to_file_csv([obj1, obj2, obj3])

        # Check if the CSV file exists
        self.assertTrue(os.path.exists("Base.csv"))

    def test_load_from_file_csv(self):
        # Create instances of the class
        obj1 = Base(1)
        obj2 = Base(2)
        obj3 = Base(3)

        # Save the instances to a CSV file
        Base.save_to_file_csv([obj1, obj2, obj3])

        # Load the instances from the CSV file
        loaded_objs = Base.load_from_file_csv()

        # Check if the loaded objects are instances of the class
        for obj in loaded_objs:
            self.assertIsInstance(obj, Base)
