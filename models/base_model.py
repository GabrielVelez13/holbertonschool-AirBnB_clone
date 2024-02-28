#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Innitializing the class. """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """ Adds to the str. """
        return ("[{}] ({}) <{}>"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ Saves the data. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Sets extra keys in the dictionary. """
        temp_dict = self.__dict__.copy()
        temp_dict["__class__"] = self.__class__.__name__
        temp_dict["created_at"] = self.created_at.strftime("\
                                        %Y-%m-%dT%H:%M:%S.%f")
        temp_dict["updated_at"] = self.updated_at.strftime("\
                                        %Y-%m-%dT%H:%M:%S.%f")
        return temp_dict
