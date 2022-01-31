#!/usr/bin/python3
""" Base Module that defines all common
    attributes/methods for other classes
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ class for creating base model objects """

    def __init__(self, *args, **kwargs):
        """ BaseModel init

            Arguments:
                    args: Keyword arguments
                    kwargs: positional arguments
        """
        if kwargs:
            for key in kwargs:
                if key not in ('created_at', 'updated_at', '__class__'):
                    setattr(self, key, kwargs[key])
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns string represenattion of the object """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ modify updated_at attribute to the current time of modification """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing allkeys/values
            of __dict__ of the instance

            a key __class__ is added to this dictionary
            with the class name of the object

            created_at and updated_at are converted to string object in ISO
            format
                  : %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
                  : isoformat() of datetime object is used
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
