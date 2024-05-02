#!/usr/bin/python3
""" contains cart class"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Cart(BaseModel, Base):
    """ define Cart classes"""
    __tablename__ = 'carts'
    #user_id = Column(String(50), ForeignKey('users.id'), nullable=False)
    # product_id = Column(String(50), ForeignKey('products.id'), nullable=False)
    #quantity = Column(Integer, nullable=False)
    #price = Column(Float, nullable=False)
    #user = relationship('User', backref='carts')
    #product = relationship('Product', backref='carts')
    items = relationship('CartItem', backref='cart')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
