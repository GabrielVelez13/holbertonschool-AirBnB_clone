#!/usr/bin/python3
"""Module test_review"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test for the Review class"""

    def setup(self):
        """Set up"""
        self.r1 = Review()

    def test_place_id(self):
        """Testing Review place_id"""
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        """Testing Review user_id"""
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        """Testing Review text"""
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Testing Review inheritance"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Testing Review attributes"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))

    def test_attribute_default(self):
        """Test attribute default"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_str(self):
        """Testing Review __str__"""
        expected = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(expected, str(self.review))

if __name__ == "__main__":
    unittest.main()
