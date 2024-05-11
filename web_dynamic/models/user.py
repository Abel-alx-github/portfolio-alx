#!/usr/bin/python3
""" create user Class"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer


class User(BaseModel, Base):
    __tablename__ = 'users'
    user_name = Column(String(255), unique=True, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

