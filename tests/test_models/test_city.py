#!/usr/bin/python3
"""Module test_city"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test for the City class"""

    def setup(self):
        """Set up"""
        self.c1 = City()

    def test_name(self):
        """Testing City name"""
        self.assertEqual(self.city.name, "")

    def test_state_id(self):
        """Testing City state_id"""
        self.assertEqual(self.city.state_id, "")

    def test_inheritance(self):
        """Testing City inheritance"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Testing City attributes"""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_attribute_default(self):
        """Test attribute default"""
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_str(self):
        """Testing City __str__"""
        expected = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(expected, str(self.city))

if __name__ == "__main__":
    unittest.main()
