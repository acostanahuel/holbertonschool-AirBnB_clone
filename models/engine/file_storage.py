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
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f) 
            
 
    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                self.__objects = data
        except FileNotFoundError:
           
            pass