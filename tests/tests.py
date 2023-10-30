#!/usr/bin/python3
"""User tests"""


import unittest
from models.user import User


class UserTests(unittest.TestCase):
    def test_user_attributes_empty(self):
        """Test if User's attributes are empty"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.password, "")
    

if __name__ == '__main__':
    unittest.main()
