#!/usr/bin/python3
""" FileStorage class """
import json
from models.base_model import BaseModel
import datetime
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj
    
    def save(self):
        with open(FileStorage.__file_path, encoding='utf-8', mode='w') as file:
            new_d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(new_d, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                self.__objects = {k: BaseModel(**v)
                                  for k, v in json.load(file).items() + ""}
        except Exception:
            pass