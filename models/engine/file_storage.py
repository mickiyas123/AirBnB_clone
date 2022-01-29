#!/usr/bin/python3
"""
File storage class
"""
import json
import os
from datetime import datetime


class FileStorage():
    """File Storage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        # if os.path.exists(FileStorage.__file_path):
        new_data = dict((k, v.to_dict())
                        for k, v in FileStorage.__objects.items())
        # with open(FileStorage.__file_path) as file:
        #     obj_data = json.load(file)
        #     obj_data.update(new_data)
        #     with open(FileStorage.__file_path, mode='w') as file:
        #         json.dump(new_data, file, indent=4)
        # else:
        #     obj_data = dict((k, v.to_dict())
        #                     for k, v in FileStorage.__objects.items())
        with open(FileStorage.__file_path, mode='w') as file:
            json.dump(new_data, file, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        from models.base_model import BaseModel
        from models.user import User
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                json_str = json.load(file)
            for k, v in json_str.items():
                # if v["__class__"] in globals():
                #     classname = globals()[v["__class__"]]
                FileStorage.__objects[k] = BaseModel(**v)
        else:
            pass
