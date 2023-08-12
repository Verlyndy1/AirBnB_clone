#!/usr/bin/python3
"""
Creates a BaseModel class that defines attributes and
methods for other classes
"""


import datetime
import uuid
import json
import models


class BaseModel:
    """Creates base model for other classes"""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif "updated_at" == key:
                    self.updated_at = datetime.datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif "created_at" == key:
                    self.created_at = datetime.datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation of the base class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the updated_at instance attribute to current time"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing keys/values of the instance"""
        dictionary = {}
        dictionary['__class__'] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        return dictionary
