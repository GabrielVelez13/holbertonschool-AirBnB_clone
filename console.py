#!/usr/bin/python3
"""Defining HBNBCommand class"""
import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Console for Airbnb clone."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Does nothing when nothing is entered"""
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        if arg not in "Basemodel":
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)




if __name__ == '__main__':
    HBNBCommand().cmdloop()
