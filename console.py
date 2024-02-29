#!/usr/bin/python3
"""Defining HBNBCommand class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console for Airbnb clone."""

    prompt = "(hbnb) "

    def do_help(self, arg: str):
        """Shows documentation of the options\n"""
        return super().do_help(arg)

    def do_quit(self, arg: str):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg: str):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
