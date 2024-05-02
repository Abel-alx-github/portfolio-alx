#!/usr/bin/python3

""" add sample data to database of fre_db """

import models
from models.product import Product
from models.category import Category


c_data = [{'name': 'clothes', 'id': 1,}, {'name': 'shoes', 'id':2 ,}, {'name': 'watches', 'id':3 ,}, {'name': 'accessories', 'id':4 ,}]

for data in c_data:
    c = Category(**data)
    c.save()

p_data = [
         {"name": "cloth..", "category_id": 1, "price": 55, "description": "best close", "image_url": "../static/image/clothes/cl0.jpg", "url": "http://127.0.0.1:5000/products/"},
	 {"name": "cloth..", "category_id": 1, "price": 55, "description": "best close", "image_url": "../static/image/clothes/cl1.jpg" , "url": "http://127.0.0.1:5000/products/"},
	 {"name": "cloth..", "category_id": 1, "price": 55, "description": "best close", "image_url": "../static/image/clothes/cl2.jpg", "url": "http://127.0.0.1:5000/products/"},
	 {"name": "cloth..", "category_id": 1, "price": 55, "description": "best close", "image_url": "../static/image/clothes/cl3.jpg", "url": "http://127.0.0.1:5000/products/"},
	 {"name": "cloth..", "category_id": 1, "price": 55, "description": "best close", "image_url": "../static/image/clothes/cl4.jpg", "url": "http://127.0.0.1:5000/products/"},
	 {"name": "cloth..", "category_id": 1, "price": 55, "description": "best close", "image_url": "../static/image/clothes/cl5.jpg", "url": "http://127.0.0.1:5000/products/"},
	 {"name": "cloth..", "category_id": 1, "price": 55, "description": "best close", "image_url": "../static/image/clothes/cl6.jpg", "url": "http://127.0.0.1:5000/products/"},
         
         {"name": "shoes..", "category_id":2 , "price":100 , "description": "best shoes", "image_url": "../static/image/shoes/sh0.jpg", "url": "http://127.0.0.1:5000/products/"},
	 {"name": "shoes..", "category_id":2 , "price":100 , "description": "best shoes", "image_url": "../static/image/shoes/sh1.jpg", "url": "http://127.0.0.1:5000/products/"},
	 {"name": "shoes..", "category_id":2 , "price":100 , "description": "best shoes", "image_url": "../static/image/shoes/sh2.jpg", "url": "http://127.0.0.1:5000/products/"},
	 {"name": "shoes..", "category_id":2 , "price":100 , "description": "best shoes", "image_url": "../static/image/shoes/sh3.jpg", "url": "http://127.0.0.1:5000/products/"},
	 {"name": "shoes..", "category_id":2 , "price":100 , "description": "best shoes", "image_url": "../static/image/shoes/sh4.jpg", "url": "http://127.0.0.1:5000/products/"},
	 {"name": "shoes..", "category_id":2 , "price":100 , "description": "best shoes", "image_url": "../static/image/shoes/sh5.jpg", "url": "http://127.0.0.1:5000/products/"},

         {"name": "watches", "category_id":3 , "price": 200, "description": "best watches", "image_url": "../static/image/wathes/wa0.jpg", "url": "http://127.0.0.1:5000/products/"},
         {"name": "watches", "category_id":3 , "price": 200, "description": "best watches", "image_url": "../static/image/wathes/wa0.jpg", "url": "http://127.0.0.1:5000/products/"},
         {"name": "watches", "category_id":3 , "price": 200, "description": "best watches", "image_url": "../static/image/wathes/wa0.jpg", "url": "http://127.0.0.1:5000/products/"},
         {"name": "watches", "category_id":3 , "price": 200, "description": "best watches", "image_url": "../static/image/wathes/wa0.jpg", "url": "http://127.0.0.1:5000/products/"},
         {"name": "watches", "category_id":3 , "price": 200, "description": "best watches", "image_url": "../static/image/wathes/wa0.jpg", "url": "http://127.0.0.1:5000/products/"},
         {"name": "watches", "category_id":3 , "price": 200, "description": "best watches", "image_url": "../static/image/wathes/wa0.jpg", "url": "http://127.0.0.1:5000/products/"},
         {"name": "watches", "category_id":3 , "price": 200, "description": "best watches", "image_url": "../static/image/wathes/wa0.jpg", "url": "http://127.0.0.1:5000/products/"},


         {"name": "accessories", "category_id":4 , "price":80 , "description": "best accessory", "image_url": "../static/image/accessories/ac0.jpg", "url": "http://127.0.0.1:5000/products/"},
         {"name": "accessories", "category_id":4 , "price":80 , "description": "best accessory", "image_url": "../static/image/accessories/ac1.jpg", "url": "http://127.0.0.1:5000/products/"},
         {"name": "accessories", "category_id":4 , "price":80 , "description": "best accessory", "image_url": "../static/image/accessories/ac2.jpg", "url": "http://127.0.0.1:5000/products/"},
         {"name": "accessories", "category_id":4 , "price":80 , "description": "best accessory", "image_url": "../static/image/accessories/ac3.jpg", "url": "http://127.0.0.1:5000/products/"},
         {"name": "accessories", "category_id":4 , "price":80 , "description": "best accessory", "image_url": "../static/image/accessories/ac4.jpg", "url": "http://127.0.0.1:5000/products/"},
         {"name": "accessories", "category_id":4 , "price":80 , "description": "best accessory", "image_url": "../static/image/accessories/ac5.jpg", "url": "http://127.0.0.1:5000/products/"},

	]

for p_d in p_data:
    p = Product(**p_d)
    p.save()


