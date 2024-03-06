#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship(
        'Place', cascade='all, delete-orphan', backref='user')

    def __str__(self):
        """Returns a string representation of the User instancce"""
        return "[{}] ({}) {}".format(
            self.__class.__name__,
            self.id,
            {column.name: getattr(
                self, column.name) for column in self.__class__.__table__.columns}
        )
