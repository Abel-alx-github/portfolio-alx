#!/usr/bin/python3

""" holds class category"""

import models
from models.base_model import BaseModel, Base
# from models.product import Product
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Category(BaseModel, Base):
    __tablename__ = "categories"  # Optional, but good practice for clarity
    name = Column(String(50), nullable=False, unique=True)
    # products = relationship("Product")

    def __init__(self, *args, **kwargs):
        """initializes product"""
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Category {self.name}>"
