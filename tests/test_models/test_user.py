#!/usr/bin/python3
"""
testing class User
"""

import unittest
from models.user import User



class test_class_user(unittest.TestCase):
    """class for testing class user"""
    my_model = User()
    
    def test_type(self):
        self.assertIsInstance(self.my_model, User)

    def test_email(self):
        """test email"""
        self.assertEqual(self.my_model.email, "")
    def test_password(self):
        """test pw """
        self.assertEqual(self.my_model.password, "")

    def test_first_name(self):
        """test fn"""
        self.assertEqual(self.my_model.first_name, "")

    def test_last_name(self):
        """test ln"""
        self.assertEqual(self.my_model.last_name, "")


if __name__ == '__main__':
    unittest.main()