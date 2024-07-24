#!/usr/bin/python3
"""
This is the BaseModel class
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The class"""
    def __init__(self, *args, **kwargs):
        """initializes a new instance of Basemodel."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """return a string representation of the instance"""
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the updated_at time with the current time"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return a dictionary containing all key/values of the instance"""
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
