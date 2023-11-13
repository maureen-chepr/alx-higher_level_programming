#!/usr/bin/python3
"""
    Test Case for Square base
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    @classmethod
    def setUpClass(cls):
        """set up the tests"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(5, 4)
        cls.r2 = Rectangle(3, 6, 2)

    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)

    def test_width(self):
        """Test for functioning width"""
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r2.width, 3)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.r1.height, 4)
        self.assertEqual(self.r2.height, 6)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 2)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)

    def test_normal_use(self):
        """Testing expected use case"""
        self.assertIsInstance(self.r1, Rectangle)
        self.assertIsInstance(self.r2, Rectangle)

    def test_None_as_first_arg(self):
        """Testing None as first argument"""
        with self.assertRaises(TypeError):
            r3 = Rectangle(None, 3)

    def test_too_many_args(self):
        """Testing too many args passed to fn"""
        with self.assertRaises(TypeError):
            r3 = Rectangle(5, 4, 7, 3, 2, 7)

    def test_area(self):
        """Testing area method fof cls Rectangle"""
        r4 = Rectangle(5, 4)
        self.assertEqual(r4.area(), 20)

    def test_negative_int(self):
        """Testing for a neg int as an arg"""
        with self.assertRaises(ValueError):
            r5 = Rectangle(5, -4)

    def test_neg_ints(self):
        """Testing for several negative int arguments"""
        with self.assertRaises(ValueError):
            r6 = Rectangle(-1, -3, -5)

    def test_kwargs(self):
        """Testing for keyword args passed to fn"""
        r7 = Rectangle(x=5, width=3, height=5, id=100, y=2)
        self.assertEqual(r7.width, 3)
        self.assertEqual(r7.y, 2)
        self.assertEqual(r7.id, 100)
        self.assertEqual(r7.x, 5)
        self.assertEqual(r7.height, 5)

    def test_print(self):
        """Testing __str__ method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 5/4")

    def test_Update(self):
        """Testing update cls Rect method"""
        r13 = Rectangle(1, 2)
        r13.update(125, 6, 4)
        self.assertEqual(str(r13), "[Rectangle] (125) 0/0 - 6/4")

    def test_string_arg(self):
        """Testing string as first arg"""
        with self.assertRaises(TypeError):
            r9 = Rectangle("nine", 6)

    def test_float_arg(self):
        """Testing float as 1st arg"""
        with self.assertRaises(TypeError):
            r10 = Rectangle(4.2, 5)

    def test_string_as_arg2(self):
        """Testing string as second arg"""
        with self.assertRaises(TypeError):
            r11 = Rectangle(5, "six", 7)

    def test_no_args(self):
        """Testing no args passed"""
        with self.assertRaises(TypeError):
            r12 = Rectangle()

    def test_dict_to_json(self):
        """Test the conversion of dictionary to JSON string."""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1_dict = r1.to_dictionary()
        r1_json = Base.to_json_string([r1_dict])
        expected_json = '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
        self.assertEqual(r1_json, expected_json)


if __name__ == "__main__":
    """if run as main modl"""
    unittest.main()
