#!/usr/bin/python3
"""Module test_place"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test for the Place class"""

    def setup(self):
        """Set up"""
        self.p1 = Place()

    def test_city_id(self):
        """Testing Place city_id"""
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """Testing Place user_id"""
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """Testing Place name"""
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """Testing Place description"""
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """Testing Place number_rooms"""
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """Testing Place number_bathrooms"""
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """Testing Place max_guest"""
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """Testing Place price_by_night"""
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """Testing Place latitude"""
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """Testing Place longitude"""
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """Testing Place amenity_ids"""
        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        """Testing Place inheritance"""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Testing Place attributes"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))


if __name__ == "__main__":
    unittest.main()
