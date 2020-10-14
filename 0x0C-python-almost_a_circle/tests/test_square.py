#!/usr/bin/python3
"""Unittest for Rectangle"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_value(unittest.TestCase):
    def test_args(self):
        """Test for 4 arguments passed in."""
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 10)

    def test_less_than_zero(self):
        """Test for zero and neg inputs"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 5, -2)


class TestSquare_type(unittest.TestCase):
    def no_arg(self):
        """passing no arugment"""
        with self.assertRaises(TypeError):
            Square()

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, None)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.5, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 4.8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 5, 2.7)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Howdy")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "Howdy")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, "Howdy")

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, (1, 2, 3))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, (1, 2, 3))

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, [1, 2, 3])

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, {1, 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 10, {1, 2, 3})

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 3, "b": 4})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {"a": 4, "b": 5})


class TestSquare_area(unittest.TestCase):
    def test_largeArea(self):
        s = Square(30000, 2, 10, 0)
        self.assertEqual(900000000, s.area())

    def test_1argArea(self):
        s = Square(5, 8, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquare_create(unittest.TestCase):
    def test_create(self):
        s1 = Square(5, 12, 3, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual((s1 == s2), False)
        self.assertEqual((s1 is s2), False)

    def test_to_dict(self):
        temp = Square(2, 4, 6, 8)
        s1 = temp.to_dictionary()
        s2 = {"id": 8, "size": 2, "x": 4, "y": 6}
        self.assertEqual(s1, s2)


class TestSquare_update(unittest.TestCase):
    def test_updateArgs(self):
        s = Square(15, 33, 14, 7)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_updateKwargs(self):
        s = Square(15, 33, 14, 7)
        s.update(id=5, size=4, x=2, y=1)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)
