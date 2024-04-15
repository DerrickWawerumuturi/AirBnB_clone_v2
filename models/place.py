#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float,  ForeignKey, DateTime

class Place(BaseModel, Base):
    """  A place to stay """
    __tablename__  = "places"
    
    city_id = Column(String(length=60), ForeignKey('city_id'),nullable=False)
    user_id = Column(String(length=60), ForeignKey('users_id'),nullable=False)
    name =  Column(String(length=128), nullable=False)
    description = Column(String(length=1024),nullable=False)
    number_rooms = Column(Integer,default=0,nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0,nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
