#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.product import Product
from models.cart import Cart
from models.cart_item import CartItem
from models.categories import Category

from models.base_model import BaseModel
import json
import os
import pep8
import unittest
from models import storage
DBStorage = db_storage.DBStorage
classes = {"Product": Product, "Category": Category, "Cart": Cart,
           "CartItem": CartItem}



class TestDbStorage(unittest.TestCase):
    """Test the DbStorage class"""
    # @unittest.skipIf(models.storage != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    # @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    # @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    #  @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""

    def test_get_db(self):
        """ Tests method for obtaining an instance db storage"""
        dic = {"id": "this_is_cartId"}
        instance = Cart(**dic)
        storage.new(instance)
        storage.save()
        get_instance = storage.get(Cart, instance.id)
        self.assertEqual(get_instance, instance)

    def test_count(self):
        """ Tests count method db storage """
        # dic = {"name": "Vecindad"}
        # product = Product(**dic)
        # storage.new(product)
        # dic = {"name": "shoes", "category": '2'}
        
        # storage.new(product)
        # storage.save()
        c = storage.count()
        self.assertEqual(len(storage.all()), c)
