#!/usr/bin/python3
"""
this module is to enable storage
of python objects as json strings
"""
import json
import os


class FileStorage:
    """The class itself"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """add an object to __objects with key className.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        convert every object in __objects to dictionary and
        then serializes the dictionary to a JSON string
        and then stores the string to the file path
        """
        object_dict = {}
        for key, obj in self.__objects.items():
            object_dict = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            (json.dump(object_dict, file))

    def classes(self):
        """return a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        classes = {"BaseModel": BaseModel}
        return classes

    def reload(self):
        """deserializes the JSON file to __objects if exists"""
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name = obj_dict["__class__"]
                    if cls_name in self.classes():
                        className = self.classes()[cls_name]
                    self.new(className(**obj_dict))
        except FileNotFoundError:
            return
