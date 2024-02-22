#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    __abstract__ = True

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
        if 'created_at' not in kwargs:
            self.created_at = datetime.utcnow()
        if 'updated_at' not in kwargs:
            self.updated_at = datetime.utcnow()

    def save(self):
        """Saves the instance to the storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """Deletes the instance from the storage"""
        models.storage.delete(self)
