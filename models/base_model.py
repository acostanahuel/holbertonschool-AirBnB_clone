#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
 
    """
    A base class for all hbnb models.
    """

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from . import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """str"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update every time obj is accsesed"""
        from . import storage
        self.updated_at = datetime.now()
        storage.save()
        

    def to_dict(self):
        """dict for seralization"""
        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
    