#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    #places = relationship("Place", backref="cities", cascade="delete")

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        from models.state import State
        states = models.storage.all(State)
        for key, obj in states.items():
            if obj.id == self.state_id:
                self.state = obj
