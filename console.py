#!/usr/bin/python3
"""Defining HBNBCommand class"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
