#!/usr/bin/python3

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
    
