#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities_rel = relationship(
            "City", back_populates="state", cascade="all, delete-orphan")

    def get_cities(self, storage):
        """Returns the list of City objects linked to the current state"""
        if not isinstance(storage, DBStorage):
            return [city for city in self.cities]
        else:
            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities

    def __str__(self):
        """Return a string representation of the State instance """
        return "[State] ({}) {} {}".format(
            self.id, self.to_dict(), self.created_at)
