#!/usr/bin/python3
"""Module that contain the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel as B

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) \
and prints the id
"""
        if line == "":
            print("** class name missing **")
        args = line.split()
        with open("file2.json", "a") as o:
            o.write(B(args[0]))
            o.write("\n")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
