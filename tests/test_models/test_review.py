#!/usr/bin/python3
"""
testing class review
"""

import unittest
from models.review import Review


class test_class_review(unittest.TestCase):
    """class for testing class review"""
    my_model = Review()

    def testName(self):
        self.assertEqual(self.my_model.place_id, "")
        self.assertEqual(self.my_model.user_id, "")
        self.assertEqual(self.my_model.text, "")
