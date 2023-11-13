#!/usr/bin/python3
"""
    Test Case for Square base
"""
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    @classmethod
    def setUpClass(cls):
        """set up the tests"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(5)
        cls.s2 = Square(5, 2)

    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)

    def test_size(self):
        """Test for functioning size"""
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s2.size, 5)

    def test_width(self):
        """Test for functioning width"""
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s2.width, 5)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.s1.height, 5)
        self.assertEqual(self.s2.height, 5)
        

if __name__ == "__main__":
    unittest.main()
