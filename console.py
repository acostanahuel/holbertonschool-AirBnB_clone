#!/usr/bin/python3
"""module that that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class the comand interpreter"""
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
