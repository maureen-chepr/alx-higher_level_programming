#!/usr/bin/python3
"""
   Test module for class Base in ../models/base.py
"""
from models.base import Base
import unittest
import json


class TestBase(unittest.TestCase):
    """
       Test class for class Base
    """
    def test_excess_args(self):
        """Testing excess args passed"""
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

    def test_no_args(self):
        """Testing no args"""
        b2 = Base()
        self.assertEqual(b2.id, 3)

    def test_neg_int(self):
        """Testing negative arg"""
        b3 = Base(-5)
        self.assertEqual(b3.id, -5)

    def test_empty_json_str(self):
        """Testing empty json string"""
        json_str = Base.to_json_string([])
        self.assertTrue(type(json_str) is str)
        self.assertEqual(json_str, '[]')

    def test_to_json_str(self):
        """Testing to_json_string method"""
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])

        assert isinstance(json_s, str)

        loaded_data = json.loads(json_s)
        assert isinstance(loaded_data, list)

        self.assertEqual(loaded_data, [d1, d2])

        assert '"id": 9' in json_s
        assert '"width": 5' in json_s

    def test_creation_with_id(self):
        """Testing creation with specified id"""
        b4 = Base(42)
        self.assertEqual(b4.id, 42)

    def test_id_after_creation_with_id(self):
        """Testing id after creation with specified id"""
        b5 = Base(42)
        self.assertEqual(b5.id, 42)
        b5.id = 99
        self.assertEqual(b5.id, 99)

    def test_creation_multiple_instances(self):
        """Testing creation of multiple instances"""
        b6 = Base()
        b7 = Base()
        self.assertNotEqual(b6.id, b7.id)

    def test_to_json_string_with_none(self):
        """Testing to_json_string method with None as argument"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        """Testing to_json_string method with an empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")


if __name__ == '__main__':
    """unittest call"""
    unittest.main()
