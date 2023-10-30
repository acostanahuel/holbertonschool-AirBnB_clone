#!/usr/bin/python3
"""
testing class city
"""

import unittest
from models.city import City



class test_class_amenity(unittest.TestCase):
    """class for testing class city"""
    my_model = City()

    def testName(self):
        self.assertEqual(self.my_model.name, "")