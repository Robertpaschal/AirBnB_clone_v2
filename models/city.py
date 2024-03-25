#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship(
        'Place', cascade='all, delete-orphan', backref='cities')
    state = relationship("State", back_populates="cities_rel")

    def __str__(self):
        """ Return a string representation of the City instance """
        state_name = self.state.name if self.state else "Unknown"
        return "[City] ({}) {} in the state: {}".format(
            self.id, self.name, state_name)
