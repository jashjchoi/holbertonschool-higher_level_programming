#!/usr/bin/python3
"""Unittest for Rectangle"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def no_arg(self):
        """Test for passing zero arugment"""
        self.assertRaises(TypeError, Rectangle, ())

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
