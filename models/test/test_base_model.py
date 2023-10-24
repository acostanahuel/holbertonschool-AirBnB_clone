#!/usr/bin/python3
"""
testing class base
"""

import unittest
import os
from models import base_model
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


def del_old_files():
    """fddsfdffdfg fg fdgf"""
    try:
        os.remove("recover_objs.json")
    except FileNotFoundError:
        pass


class test_class_base(unittest.TestCase):
    """class for testing class base model"""
    """# Global variables"""
    file_storage = FileStorage()
    test = BaseModel()

    @classmethod
    def setUpClass(self):
        """set class"""
        self.my_model = BaseModel()

    def setUp(self):
        """ set attr """
        self.dict = self.my_model.to_dict()

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(base_model.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_create_base(self):
        """test instance class BaseModel"""
        self.assertIsInstance(self.my_model, BaseModel)

    def test_attr(self):
        """test attributes"""
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)

        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.assertIn("name", self.my_model.to_dict())
        self.assertIn("my_number", self.my_model.to_dict())
        self.dict = self.my_model.to_dict()
        self.assertEqual(self.dict["my_number"], 89)
        self.assertEqual(self.dict["name"], "My First Model")

    def test_create_kwargs(self):
        """ create class from dictionary """
        self.kwargs = BaseModel(self.dict)
        self.assertIsInstance(self.kwargs, BaseModel)

    def test_update(self):
        """ test update date """
        update_old = self.my_model.updated_at
        self.my_model.save()
        update_new = self.my_model.updated_at
        self.assertTrue(update_old != update_new)

    def test_to_dict(self):
        """test_to_dict """
        bm = BaseModel()
        dic = bm.to_dict()
        self.assertEqual(type(dic), dict)
        self.assertTrue(type(dic['created_at']) is str)
        self.assertTrue(type(dic['updated_at']) is str)

    def test_id(self):
        """Test the id attribute."""
        test_dict = {}
        for index in range(1, 101):
            test_dict[f"model{index}"] = BaseModel()
        for index, value in enumerate(test_dict.values(), 1):
            self.assertNotEqual(value.id, test_dict.get(
                f"model{index + 1}", self.test).id
            )

    def test_created_at(self):
        """Test create_at attribute."""
        test_dict = {}
        for index in range(1, 20):
            test_dict[f"model{index}"] = BaseModel()
        for index, value in enumerate(test_dict.values(), 1):
            self.assertNotEqual(value.created_at, test_dict.get(
                f"model{index + 1}", self.test).created_at
            )

    def test_save(self):
        """Test saving the model."""
        with open("recover_objs.json", "w", encoding="UTF-8") as json_file:
            json.dump({}, json_file)
        update_time = self.test.updated_at
        self.file_storage.save()
        self.test.save()
        BaseModel.save(self)
        self.assertTrue(update_time < self.test.updated_at)
        with open("recover_objs.json", encoding="UTF-8"):
            pass
        del_old_files()

    def test_to_dict(self):
        """Test to_dict method."""
        test_dict = self.test.to_dict()

    def test__str__(self):
        """Test __str__ special method."""
        self.assertEqual(str(self.test)[:11], "[BaseModel]")

    def test_json_deserializing(self):
        test_new_model = self.test.to_dict()
        new_model = BaseModel(**test_new_model)
        self.assertIsInstance(new_model, BaseModel)

if __name__ == '__main__':
    unittest.main()