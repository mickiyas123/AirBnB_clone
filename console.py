#!/usr/bin/python3
"""
The Console
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        """Exits the cmd interpreter"""
        print()
        return True

    def do_quit(self, arg):
        """Exits the cmd interpreter"""
        quit()

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it amd prints its id"""
        if arg:
            if arg in globals():
                classname = globals()[arg]
                new_obj = classname()
                new_obj.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance
based on the class name and id"""
        args = arg.split()
        if args:
            try:
                eval(args[0])
                obj_key = args[0] + '.' + args[1]
                all_objs = storage.all()
                print(all_objs[obj_key])
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")
            except KeyError:
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
and id (saves the changes into the JSON file)."""
        args = arg.split()
        if args:
            try:
                eval(args[0])
                obj_key = args[0] + '.' + args[1]
                all_objs = storage.all()
                del all_objs[obj_key]
                storage.save()
            except IndexError:
                print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")
            except KeyError:
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """ Prints all string representation of all instances based
or not on the class name."""
        objs_list = []
        all_objs = storage.all()
        if arg:
            if arg in globals():
                classname = globals()[arg]
                for obj in all_objs.values():
                    if isinstance(obj, classname):
                        objs_list.append(str(obj))
                print(objs_list)
            else:
                print("** class doesn't exist **")
        else:
            for obj in all_objs.values():
                objs_list.append(str(obj))
            print(objs_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
by adding or updating attribute (saves the changes into the JSON file)."""
        args = shlex.split(arg)
        all_objs = storage.all()
        if args:
            if len(args) == 1:
                if args[0] in globals():
                    print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
            elif len(args) == 2:
                if args[0] in globals():
                    obj_key = args[0] + '.' + args[1]
                    if obj_key in all_objs:
                        print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(args) == 3:
                if args[0] in globals():
                    obj_key = args[0] + '.' + args[1]
                    if obj_key in all_objs:
                        print("** value missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            elif len(args) > 3:
                if args[0] in globals():
                    obj_key = args[0] + '.' + args[1]
                    if obj_key in all_objs:
                        new_obj = all_objs[obj_key]
                        if args[3].isdigit():
                            args[3] = int(args[3])
                        else:
                            try:
                                float(args[3])
                                args[3] = float(args[3])
                            except ValueError:
                                pass
                        setattr(new_obj, args[2], args[3])
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()