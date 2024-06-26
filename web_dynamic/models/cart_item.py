#!/usr/bin/python3
""" module contains cart class"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class CartItem(BaseModel, Base):
    """ define Cart classes """
    __tablename__ = 'cart_items'
    cart_id =  Column(String(50), ForeignKey('carts.id'), primary_key=True)
    product_id = Column(String(50), ForeignKey('products.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    url = Column(String(250))
   
    def __init__(self, *args, **kwargs):
        # init inherited BaseModel class
        super().__init__(*args, **kwargs)
    
    
