#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent an abstracted storage engine."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objetcs obj with key <obj_class_name>.id"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict.update([(key, value.to_dict())])
        with open(self.__file_path, "w", encoding='UTF-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """reloads objects and save to dic"""
        try:
            with open(self.__file_path) as file:
                for key, value in json.load(file).items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
