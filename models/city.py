#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.state import State
from models import storage


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    #places = relationship("Place", backref="cities", cascade="delete")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        states = storage.all(State)
        for key, state in states.items():
            if state.id == self.state_id:
                self.state = state
