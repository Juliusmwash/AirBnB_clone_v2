#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """
        Instanciate City class and builds a relationship
        with the State class
        """
        super().__init__(**kwargs)
        from models.state import State
        if getenv("HBNB_TYPE_STORAGE") == "db":
            states = models.storage.all(State)
            for key, obj in states.items():
                if obj.id == self.state_id:
                    self.state = obj
