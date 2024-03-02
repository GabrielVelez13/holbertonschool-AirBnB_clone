#!/usr/bin/python3
"""Module test_state"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test for the State class"""

    def setup(self):
        """Set up"""
        self.s1 = State()

    def test_name(self):
        """Testing State name"""
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Testing State inheritance"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Testing State attributes"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_attribute_default(self):
        """Test attribute default"""
        self.assertEqual(self.state.name, "")

    def test_str(self):
        """Testing State __str__"""
        expected = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(expected, str(self.state))

if __name__ == "__main__":
     unittest.main()
