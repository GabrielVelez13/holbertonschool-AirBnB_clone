#!/usr/bin/python3
"""Module test_amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test for the Amenity class"""

    def setup(self):
        """Set up"""
        self.a1 = Amenity()

    def test_name(self):
        """Testing Amenity name"""
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """Testing Amenity inheritance"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Testing Amenity attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_attribute_default(self):
        """Test attribute default"""
        self.assertEqual(self.amenity.name, "")

    def test_str(self):
        """Testing Amenity __str__"""
        expected = "[Amenity] ({}) {}"
        expected = expected.format(self.amenity.id, self.amenity.__dict__)

        self.assertEqual(expected, str(self.amenity))

if __name__ == "__main__":
    unittest.main()
