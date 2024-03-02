#!/usr/bin/python3
"""Module test_base_model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for the BaseModel class"""

    def test_id(self):
        """Testing BaseMoodel id"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_created_at(self):
        """Testing BaseMoodel created_at"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.created_at, b2.created_at)

    def test_updated_at(self):
        """Testing BaseMoodel updated_at"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.updated_at, b2.updated_at)

    def test_str(self):
        """Testing BaseMoodel __str__"""
        b1 = BaseModel()
        self.assertEqual(str(b1), "[BaseModel] ({}) {}"
                         .format(b1.id, b1.__dict__))

    def test_save(self):
        """Testing BaseMoodel save"""
        b1 = BaseModel()
        b1.save()
        self.assertNotEqual(b1.created_at, b1.updated_at)

    def test_to_dict(self):
        """Testing BaseMoodel to_dict"""
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertEqual(b1_dict["__class__"], "BaseModel")
        self.assertEqual(b1_dict["created_at"], b1.created_at.isoformat())
        self.assertEqual(b1_dict["updated_at"], b1.updated_at.isoformat())
        self.assertEqual(b1_dict["id"], b1.id)
        self.assertEqual(b1_dict, b1.to_dict())

    def test_kwargs(self):
        """Testing BaseMoodel kwargs"""
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        b2 = BaseModel(**b1_dict)
        self.assertEqual(b1.to_dict(), b2.to_dict())
        self.assertEqual(b1.created_at, b2.created_at)
        self.assertEqual(b1.updated_at, b2.updated_at)
        self.assertEqual(b1.id, b2.id)


if __name__ == "__main__":
    unittest.main()
