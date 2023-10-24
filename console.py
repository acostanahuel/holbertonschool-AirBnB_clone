#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        return True
    
    def do_help(self, line):
        if line == "":
            print("\nDocumented commands (type help <topic>): \n\
========================================\n\
EOF  help  quit\n")
        else:
            super().do_help(line)
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
