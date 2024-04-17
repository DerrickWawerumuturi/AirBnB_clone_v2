#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float,  ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.review import Review
class Place(BaseModel, Base):
    """  A place to stay """
    __tablename__  = "places"
    
    city_id = Column(String(length=60), ForeignKey('cities_id'),nullable=False)
    user_id = Column(String(length=60), ForeignKey('users_id'),nullable=False)
    name =  Column(String(length=128), nullable=False)
    description = Column(String(length=1024),nullable=False)
    number_rooms = Column(Integer,default=0,nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0,nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = relationship('Review', backref='place', cascade="all, delete")
    
    """ getter method """
    @property
    def review(self):
        from models import storage
        review_list = []
        for review in storage.all(Review).values():
            if review.state_id == self.id:
                review_list.append(review)
                
        return review_list