#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """Representation of state """
    __tablename__ = 'products'
    name = Column(String(128), nullable=False)
    description = Column(String(256))
    price = Column(Float, nullable=False)
    image_url = Column(String(256))
    category_id = Column(String(50), ForeignKey('categories.id'))
    url =  Column(String(256))
    # category = relationship('Category', backref='products', lazy=True)

    def __init__(self, *args, **kwargs):
        """initializes product"""
        super().__init__(*args, **kwargs)
