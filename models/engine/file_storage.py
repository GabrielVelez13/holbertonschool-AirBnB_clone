#!/usr/bin/python3
""" FileStorage class """
import json
from models.base_model import BaseModel
import datetime
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes instances to a JSON file and deserializes JSON file
    to instances.
    ATTRIBUTES:
    __file_pathh is a private class attribute (str) path to the JSON file
    __objects is a private class attribute (dict) that is empty but will
    store all objects by <class name>.id ex: to store a BaseModel object
    with id=12121212, the key will be BaseModel.12121212)
    PUBLIC INSTANCE METHODS
    all():
    new(obj):
    save():
    reload():
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all method that returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ new method sets in __objects the obj with
        key <obj class name>.id """
        key = type(obj).__name__ + '.' + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ save method serializes __objects to the JSON file
        (path: __file_path) """
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesnt exist,
        no exception should be raised) """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                self.__objects = {
                    k: BaseModel(**v) for k, v in json.load(file).items()}
        except Exception:
            pass
