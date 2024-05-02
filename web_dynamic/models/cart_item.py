#!/usr/bin/python3
""" contains cart class"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class CartItem(BaseModel, Base):
    """ define Cart classes"""
    __tablename__ = 'cart_items'
    #user_id = Column(String(50), ForeignKey('users.id'), nullable=False)
    cart_id =  Column(String(50), ForeignKey('carts.id'), primary_key=True)
    product_id = Column(String(50), ForeignKey('products.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    url = Column(String(250))
    #price = Column(Float, nullable=False)
    #user = relationship('User', backref='carts')
    #product = relationship('Product', backref='carts')
    #items = relationship('CartItem', backref='cart')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    
