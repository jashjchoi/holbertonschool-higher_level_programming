#!/usr/bin/python3
"""Unittest for Rectangle"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_value(unittest.TestCase):
    def test_args(self):
        """Test for five arguments passed in."""
        r = Rectangle(5, 8, 2, 3, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 10)

    def test_less_than_zero(self):
        """Test for zero and neg inputs"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 5, -4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 5, 4, -2)


class TestRectangle_type(unittest.TestCase):
    def no_arg(self):
        """passing no arugment"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, None)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.5, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 1.5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 5, 4.8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 5, 4, 2.7)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Howdy", 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "Howdy")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, "Howdy")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 3, 5, "Howdy")

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, (1, 2, 3))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, (1, 2, 3))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, (1, 2, 3))

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, [1, 2, 3])

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2}, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {1, 2})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 10, {1, 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 10, 15, {1, 2, 3})

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 2, "b": 3})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 3, "b": 4})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"a": 4, "b": 5})


class TestRectangle_area(unittest.TestCase):
    def test_largeArea(self):
        r = Rectangle(5000000, 100000000, 2, 10, 1)
        self.assertEqual(500000000000000, r.area())

    def test_1argArea(self):
        r = Rectangle(5, 8, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_create(unittest.TestCase):
    def test_create(self):
        r1 = Rectangle(5, 12, 3)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual((r1 == r2), False)
        self.assertEqual((r1 is r2), False)

    def test_to_dict(self):
        temp = Rectangle(1, 2, 4, 6, 8)
        r1 = temp.to_dictionary()
        r2 = {"id": 8, "width": 1, "height": 2, "x": 4, "y": 6}
        self.assertEqual(r1, r2)


class TestRectangle_update(unittest.TestCase):
    def test_updateArgs(self):
        r = Rectangle(15, 33, 14, 7)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_updateKwargs(self):
        r = Rectangle(15, 33, 14, 7)
        r.update(id=5, width=4, height=3, x=2, y=1)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
