#!/usr/bin/python3
"""Module that contain the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program.
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) \
and prints the id.
"""
        if line == "":
            print("** class name missing **")
        else:
            args = line.split()
            my_model = BaseModel()
            my_model.name = args[0]
            my_model.save()
            print(my_model.id)
        return False
    
    def do_show(self, line):
        """Prints the string representation of an instance based on the \
class name and id."""
        classes = ["BaseModel","Amenity","City","Place","Review","State",
            "User"]
        args = line.split()
        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
                print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            search = f"{args[0]}.{args[1]}"
            inst = storage.all()
            if search in inst:
                print(inst[search])
            else:
                print("** no instance found **")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
