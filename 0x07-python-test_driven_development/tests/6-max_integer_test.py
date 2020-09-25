#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for unittest of max_integer program"""

    def test_posint(self):
        """ tests list of positive integers"""
        test_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)

    def test_empty(self):
        """ tests if list is empty or zero"""
        test_list = []
        self.assertEqual(max_integer(test_list), None)

    def test_zero(self):
        test_list = [0, 0, 0, 0]
        self.assertEqual(max_integer(test_list), 0)

    def test_single_int(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_max_neg(self):
        """ tests list with negative integer"""
        test_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(test_list), -1)

    def test_one_number(self):
        """ tests if list has only one number"""
        self.assertEqual(max_integer([3]), 3)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'H'])

    def test_tuple(self):
        with self.assertRaises(TypeError):
            max_integer([1, (3, 5), 7])

    def test_dict(self):
        with self.assertRaises(KeyError):
            max_integer({'k': 1, 'v': 2})


if __name__ == '__main__':
    unittest.main()
