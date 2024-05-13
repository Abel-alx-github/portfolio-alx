#!/usr/bin/python3
""" contains module for cart class defination"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Cart(BaseModel, Base):
    """ define Cart classes"""
    __tablename__ = 'carts'
    items = relationship('CartItem', backref='cart')
    
    def __init__(self, *args, **kwargs):
        # init the inherited class from BaseModel
        super().__init__(*args, **kwargs)
    
