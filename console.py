#!/usr/bin/python3
"""creates a command line interpreter for manipulating objects"""


import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """creates the console class"""
    prompt = "(hbnb) "

    def emptyline(self):
        """
        does nothing when an empty line is passed as the command
        """
        pass

    def do_quit(self, line):
        """
        quits the console program
        """
        return True

    def do_EOF(self, line):
        """
        quits the console program when EOF command is entered
        """
        print()
        return True

    def do_create(self, class_name):
        """
        creates a new instance of the a Class and stores in json
        """
        if not class_name:
            print("** class name missing **")
        # checks if the class_name key is in my_classes dict
        elif class_name not in storage.my_classes.keys():
            print("** class doesn't exist **")
        else:
            # creates new object using object value in my_classes dict
            obj = storage.my_classes[class_name]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """
        shows an instance with given class and id
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in storage.my_classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        destroys an instance with given class and id
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in storage.my_classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        prints string representation of all objects in a class
        or of all classes
        """
        obj_list = []
        args = line.split()
        object_dict = storage.all()
        if len(args) == 0:
            for obj in object_dict.values():
                obj_list.append(str(obj))
            print(obj_list)
        elif len(args) == 1:
            if args[0] not in storage.my_classes:
                print("** class doesn't exist **")
            else:
                for key in object_dict.keys():
                    if args[0] in key:
                        obj = object_dict[key]
                        obj_list.append(str(obj))
                print(obj_list)

    def do_update(self, line):
        """
        updates an instance's attribute
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in storage.my_classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(arg[0], arg[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            obj = storage.all()[key]
            cast = type(eval(arg[3]))
            arg3 = arg[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(obj, arg[2], arg3)
            obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
