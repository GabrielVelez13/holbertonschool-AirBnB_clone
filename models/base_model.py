#!/usr/bin/python3
"""Defining the basemodel of airbnb clone"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Innitializing the class. """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    time_format = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Adds to the str. """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Saves the data. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Sets extra keys in the dictionary. """
        temp_dict = self.__dict__.copy()
        temp_dict["created_at"] = self.created_at.isoformat()
        temp_dict["updated_at"] = self.updated_at.isoformat()
        temp_dict["__class__"] = self.__class__.__name__
        return temp_dict
