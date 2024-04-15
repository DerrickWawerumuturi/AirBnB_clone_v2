#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class City(BaseModel):
    """ The city class, contains state ID and name """
    
    """ Adding class attributes """
    __tablename__ = "cities"
    name = Column(String(length=128), nullable=False)
    state_id = Column(String(length=60), ForeignKey('states.id'), nullable=False)