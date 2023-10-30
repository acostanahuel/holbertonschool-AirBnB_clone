#!/usr/bin/python3
"""Module that contain a console with al his commands"""

import cmd
from models.base_model import BaseModel
from models import storage
import sys
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
           }


class HBNBCommand(cmd.Cmd):
    """The console with te commands:
    create, show, update, all, help, EOF, quit and destroy"""
    prompt = "(hbnb) "
    classes = ["BaseModel",
               "Amenity",
               "City",
               "Place",
               "Review",
               "State",
               "User"]

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
        """Creates a new instance of BaseModel, saves it (to the JSON file)
 and prints the id."""
        if line == "":
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            my_model = getattr(sys.modules[__name__], line)()
            my_model.save()
            print(my_model.id)
        return False

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id."""
        args = line.split()
        if args == []:
            print("** class name missing **")
        elif args[0] not in self.classes:
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

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the
 change into the JSON file)."""
        args = line.split()
        if args == []:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            search = f"{args[0]}.{args[1]}"
            inst = storage.all()
            if search in inst:
                del storage.all()[search]
                storage.save()
            else:
                print("** no instance found **")
        return False

    def do_all(self, line):
        """Prints all string representation of all instances based or not on
 the class name. """
        args = line.split()
        if len(args) == 0:
            a_list = []
            _all = storage.all()
            for x, i in _all.items():
                a_list.append(str(i))
            print(a_list)
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            all = storage.all()
            a_list = []
            for x, inst in all.items():
                if x.split(".")[0] == args[0]:
                    a_list.append(str(inst))
            print(a_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
 updating attribute (save the change into the JSON file)."""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            search = f"{args[0]}.{args[1]}"
            if search not in storage.all().keys():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                atributte_name = args[3]
                update = storage.all()[search]
                update.__setattr__(args[2], atributte_name)
                update.save()
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
