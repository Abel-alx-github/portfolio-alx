#!/usr/bin/python3

""" models contains class category"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Category(BaseModel, Base):
   """ define class Category"""
    __tablename__ = "categories" 
    name = Column(String(50), nullable=False, unique=True)
   
    def __init__(self, *args, **kwargs):
        """initializes product"""
        super().__init__(*args, **kwargs)

    def __repr__(self):
       # return Category {name}
       return f"<Category {self.name}>"
