#!/usr/bin/python3
"""creates the FileStorage class used for storing data"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """File storage class for storing data"""
    __objects = {}
    __file_path = "file.json"
    my_classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """
        adds a created object to the __objects dictionary
        Args:
            obj: new object to be added to dictionary
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        saves the dictionary representation of the objects in
         __object to the __file_path
        """
        new_dict = {}
        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()

        with open(self.__file_path, "w") as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        """
        deserialises content of json file to __objects dicitonary
        """
        try:
            with open(self.__file_path, "r") as f:
                # retrieves the dictionary from the json file
                object_dict = json.load(f)

            for object_data in object_dict.values():
                class_name = self.my_classes[object_data["__class__"]]

                # use class name to make new object and add to __objects
                self.new(class_name(**object_data))

        except FileNotFoundError:
            pass
