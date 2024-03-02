#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

        def __init__(self, *args, **kwargs):
            """Constructor"""
            super().__init__(*args, **kwargs)
            models.storage.new(self)

        def __str__(self):
            """String method"""
            return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

        def save(self):
            """Save method"""
            self.updated_at = datetime.now()
            models.storage.save()

        def to_dict(self):
            """To dictionary method"""
            new_dict = self.__dict__.copy()
            new_dict["__class__"] = self.__class__.__name__
            new_dict["created_at"] = self.created_at.isoformat()
            new_dict["updated_at"] = self.updated_at.isoformat()
            return new_dict
