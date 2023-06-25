#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id', String(60),
               ForeignKey('places.id'),
               primary_key=True,
               nullable=False),
        Column('amenity_id', String(60),
               ForeignKey('amenities.id'),
               primary_key=True,
               nullable=False)
        )


class Place(BaseModel, Base):
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
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Instanciates class Place and sets its relationship
        with the class User
        """
        super().__init__(**kwargs)
        from models.user import User
        from models.city import City
        if getenv("HBNB_TYPE_STORAGE", None) == "db":
            users = models.storage.all(User)
            cities = models.storage.all(City)
            for obj in users.values():
                if obj.id == self.user_id:
                    self.user = obj
                    break
            for obj in cities.values():
                if obj.id == self.city_id:
                    self.cities = obj
                    break

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Get linked Amenities."""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """add amenity id to amenity_ids"""
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
