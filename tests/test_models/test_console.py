#!/usr/bin/python3
"""unittest of the console"""
import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Test case class for testing the HBNBCommand class.
    """

    def setUp(self):
        """Set up for the tests"""
        self.cmd = HBNBCommand()

    def test_instantiation(self):
        """Test instantiation of HBNBCommand"""
        self.assertIsInstance(self.cmd, HBNBCommand)


if __name__ == '__main__':
    unittest.main()
