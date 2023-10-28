#!/usr/bin/python3
"""Module that contain the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel

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
        my_model = BaseModel()
        my_model.name = str(args[0])
        my_model.save()
        print(my_model.id)
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
