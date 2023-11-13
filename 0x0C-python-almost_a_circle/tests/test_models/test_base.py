#!/usr/bin/python3
"""
    Test case for Base class
"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Tests for base class"""
    def test_normal(self):
        b1 = Base(50)
        self.assertIsInstance(b1, Base)

if __name__ == '__main__':
    """Unit test call"""
    unittest.main()
