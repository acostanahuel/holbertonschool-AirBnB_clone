#!/usr/bin/python3
"""
testing class State
"""

import unittest
from models.state import State
from models.engine.file_storage import FileStorage



class test_class_state(unittest.TestCase):
    """class for testing class state"""
    my_model = State()

    def testName(self):
        self.assertEqual(self.my_model.name, "")

    def testStateId(self):
        self.assertEqual(self.my_model.state_id, "")