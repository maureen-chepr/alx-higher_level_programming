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

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 2)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        
    def test_normal_use(self):
        """Testing expected use case"""
        self.assertIsInstance(self.s1, Square)
        self.assertIsInstance(self.s2, Square)

    def test_None_as_first_arg(self):
        """Testing None as first argument"""
        with self.assertRaises(TypeError):
            s3 = Square(None, 3)

    def test_too_many_args(self):
        """Testing too many args passed to fn"""
        with self.assertRaises(TypeError):
            s3 = Square(5, 4, 7, 3, 2)

    def test_area(self):
        """Testing area method fof cls Square"""
        s4 = Square(5)
        self.assertEqual(s4.area(), 25)

    def test_negative_int(self):
        """Testing for a neg int as an arg"""
        with self.assertRaises(ValueError):
            s5 = Square(-5)

    def test_neg_ints(self):
        """Testing for several negative int arguments"""
        with self.assertRaises(ValueError):
            s6 = Square(-1, -3, -5)

    def test_kwargs(self):
        """Testing for keyword args passed to fn"""
        s7 = Square(size=5, x=3, id=100, y=2)
        self.assertEqual(s7.size, 5)
        self.assertEqual(s7.y, 2)
        self.assertEqual(s7.id, 100)
        self.assertEqual(s7.x, 3)

    def test_print(self):
        """Testing __str__ method"""
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 5" )

#    def test_toDictionary(self):
        """Testing to_dictionary Square method """
 #       s8 = Square(5)
  #      self.assertEqual(s8.to_dictionary(), {"id": 8, "x": 0, "size": 5, "y": 0})

    def test_Update(self):
        """Testing update cls Sqr method"""
        s13 = Square(1)
        s13.update(110, 8)
        self.assertEqual(str(s13), "[Square] (110) 0/0 - 8")

    def test_string_arg(self):
        """Testing string as first arg"""
        with self.assertRaises(TypeError):
            s9 = Square("nine")

    def test_float_arg(self):
        """Testing float as 1st arg"""
        with self.assertRaises(TypeError):
            s10 = Square(4.2)

    def test_string_as_arg2(self):
        """Testing string as second arg"""
        with self.assertRaises(TypeError):
            s11 = Square(5, "six")

    def test_no_args(self):
        """Testing no args passed"""
        with self.assertRaises(TypeError):
            s12 = Square()
    
    def test_dict_to_json(self):
        """Test the conversion of dictionary to JSON string."""
        s1 = Square(5, 2, 3, 4)
        s1_dict = s1.to_dictionary()
        s1_json = Base.to_json_string([s1_dict])
        expected_json = '[{"id": 4, "size": 5, "x": 2, "y": 3}]'
        self.assertEqual(s1_json, expected_json)

if __name__ == "__main__":
    """if run as main model"""
    unittest.main()

