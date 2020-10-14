#!/usr/bin/python3
"""Tests for tha base"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class test_Base(unittest.TestCase):
    def test_default(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_manyArgs_id(self):
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_neg_id(self):
        self.assertEqual(-5, Base(-5).id)

    def test_zero_id(self):
        self.assertEqual(0, Base(0).id)

    def test_float_id(self):
        self.assertEqual(1.5, Base(1.5).id)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_noneDict(self):
        b = Base()
        self.assertEqual(b.to_json_string(None), "[]")

    def test_reg_dict_to_string(self):
        b = Base()
        tmp = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(type(b.to_json_string(tmp)), str)

if __name__ == "__main__":
    unittest.main()
