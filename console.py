#!/usr/bin/python3
"""Defining HBNBCommand class"""
import cmd
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console for Airbnb clone."""

    prompt = "(hbnb) "
    class_dict = {
        "BaseModel": BaseModel,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "User": User,
        "Review": Review,
        "State": State
    }

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
        try:
            new_instance = eval(arg)
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        all_objs = storage.all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        else:
            if args[0] not in globals():
                print("** class doesn't exist **")
                return
            print([str(obj)
                  for key, obj in all_objs.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (value should be without double quotes).
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        obj = all_objs[key]
        value = args[3].strip("\"")
        setattr(obj, args[2], value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
