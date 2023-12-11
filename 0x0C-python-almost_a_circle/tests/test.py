#!/usr/bin/python3
'''Test cases for the Base class
'''

import unittest
b1 = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    # Valid list cases with numbers:
    def test_int(self):
        """ int numbers list"""
        listt = [1, 4, 6, 98]
        maxx = max_integer(listt)
        self.assertEqual(maxx, 98)

    def test_float_list(self):
        """ Test a float list"""
        listt = [1, 6.4, 6.8, 9.8]
        maxx = max_integer(listt)
        self.assertEqual(maxx, 9.8)

    def test_neg_list(self):
        """ Test a negative & positive list"""
        listt = [-1, 6, 6, -9]
        maxx = max_integer(listt)
        self.assertEqual(maxx, 6)

    def test_mix_list(self):
        """ Test a negative & positive list with floats"""
        listt = [-1, 6.4, 6.8, -9.8]
        maxx = max_integer(listt)
        self.assertEqual(maxx, 6.8)

    def test_eq_list(self):
        """ Test a list with equals numbers"""
        listt = [1, 1, 1, 1]
        maxx = max_integer(listt)
        self.assertEqual(maxx, 1)

    def test_ordered_list(self):
        """ Test an ordered list"""
        listt = [100, 200, 300, 400]
        maxx = max_integer(listt)
        self.assertEqual(maxx, 400)

    def test_start_list(self):
        """ Test a list with the 1st element is the max"""
        listt = [6, 3, 2, 1]
        maxx = max_integer(listt)
        self.assertEqual(maxx, 6)

    def test_one_list(self):
        """ Test a list with one numbers"""
        listt = [1]
        maxx = max_integer(listt)
        self.assertEqual(maxx, 1)

    # valid string with strings

    def test_string_comp_list(self):
        """ Test a string"""
        listt = "HIBA"
        maxx = max_integer(listt)
        self.assertEqual(maxx, 'I')

    def test_str_list(self):
        """ Test a string list"""
        listt = ["Hey", "Its me", "How are"]
        maxx = max_integer(listt)
        self.assertEqual(maxx, "Its me")

    def test_chr_list(self):
        """ Test a char list"""
        listt = ["H", "I", "g"]
        maxx = max_integer(listt)
        self.assertEqual(maxx, "g")

    def test_empty_list(self):
        """ Test an empty list"""
        listt = []
        maxx = max_integer(listt)
        self.assertEqual(maxx, None)

    def test_empty_str_list(self):
        """ Test an empty string"""
        listt = ""
        maxx = max_integer(listt)
        self.assertEqual(maxx, None)

    def test_empty_tuble_list(self):
        """ Test an empty string"""
        listt = ()
        maxx = max_integer(listt)
        self.assertEqual(maxx, None)


if __name__ == '__main__':
    unittest.main()
