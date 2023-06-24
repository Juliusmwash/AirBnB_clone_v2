#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Instanciates class Place and sets its relationship
        with the class User
        """
        super().__init__(**kwargs)
        from models.user import User
        from models.city import City
        if getenv("HBNB_TYPE_STORAGE") == "db":
            users = models.storage.all(User)
            cities = models.storage.all(City)
            for key, obj in users.items():
                if obj.id == self.user_id:
                    self.user = obj
                    break
            for key, obj in cities.items():
                if obj.id == self.city_id:
                    self.cities = obj
                    break
