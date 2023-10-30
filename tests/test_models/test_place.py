#!/usr/bin/python3
"""
testing class Place
"""

import unittest
from models.place import Plase



class test_class_place(unittest.TestCase):
    """class for testing class place"""
    my_model = Place()

    def test_place_attributes(self):
        self.assertEqual(self.my_model.city_id, "")
        self.assertEqual(self.my_model.user_id, "")
        self.assertEqual(self.my_model.name, "")
        self.assertEqual(self.my_model.description, "")
        self.assertEqual(self.my_model.number_rooms, 0)
        self.assertEqual(self.my_model.number_bathrooms, 0)
        self.assertEqual(self.my_model.max_guest, 0)
        self.assertEqual(self.my_model.price_by_night, 0)
        self.assertEqual(self.my_model.latitude, 0.0)
        self.assertEqual(self.my_model.longitude, 0.0)
        self.assertEqual(self.my_model.amenity_ids, [])