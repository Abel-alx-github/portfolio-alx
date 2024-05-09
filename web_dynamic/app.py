#!/usr/bin/python3

from flask import Flask, render_template, jsonify, session, request
from flask_cors import CORS
from models import storage
from models.product import Product
from models.cart import Cart
from models.cart_item import CartItem
from cart_operation import *
import uuid

app = Flask(__name__)
CORS(app)

@app.teardown_appcontext
def close_db(error):
    storage.close()

@app.route('/index.html')
def home():
    return render_template("index.html")


@app.route('/clothes.html')
def clothe():
    return render_template("clothes.html")

@app.route('/clothes', methods=['GET'], strict_slashes=False)
def get_clothes():
    # from .models import storage
    products = storage.all(Product).values()
    product_list = [
        {"id": p.id, "name": p.name, "price": p.price, "image_url": p.image_url, "url": p.url + p.id} for p in products if p.category_id == "1" ]
    return jsonify({'products': product_list})
    # return render_templete('')
     

@app.route('/shoes', methods=['GET'], strict_slashes=False)
def get_shoes():
    products = storage.all(Product).values()
    product_list = [
        {"id": p.id, "name": p.name, "price": p.price, "description": p.description, "image_url": p.image_url, "url": p.url + p.id} for p in products if p.category_id == "2" ]
    return jsonify({'products': product_list})
   

@app.route('/watches', methods=['GET'], strict_slashes=False)
def get_watches():
    products = storage.all(Product).values()
    product_list = [
        {"id": p.id, "name": p.name, "price": p.price, "description": p.description, "image_url": p.image_url, "url": p.url + p.id} for p in products if p.category_id == "3" ]
    return jsonify({'products': product_list})


@app.route('/accessories', methods=['GET'], strict_slashes=False)
def get_accessories():
    products = storage.all(Product).values()
    product_list = [
        {"id": p.id, "name": p.name, "price": p.price, "description": p.description, "image_url": p.image_url, "url": p.url + p.id} for p in products if p.category_id == "4" ]
    return jsonify({'products': product_list})

@app.route('/products/<id>', methods=['GET'], strict_slashes=False)
def get_product_by_id(id):
    product = storage.get(Product, id)
    if not product:
        return jsonify({'products': "not found"}), 404

    product_list = [
                     {"id": product.id, "name": product.name, "price": product.price,
                      "description": product.description, "image_url": product.image_url,
                      "url": product.url + product.id}
                   ]
    return jsonify({'products': product_list}), 200

@app.route('/cart/add', methods=['POST'], strict_slashes=False)
def addToCart():
    try:
        product_id = request.json.get("productId")
        quantity = request.json.get("quantity", 1)
        cart_id = request.json.get('cartId')
        url = request.json.get('url')
        new_cart = storage.get(Cart, cart_id)
        if not new_cart:
            new_cart = Cart(id=cart_id) 
            new_cart.save()
        product = storage.get(Product, product_id)
        if not product:
            return jsonify({"error": 'product not found'}), 404
        cart_items = storage.all(CartItem).values()
        #    print("cart_items=", cart_items)
        updated = False
        for item in cart_items:
            if item.product_id == product_id and item.cart_id == cart_id:
                item.quantity += quantity
                item.save()
                return jsonify({'message' : 'product addded/updated to cart'})
        cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity, url=url)
        cart_item.save()


        return jsonify({'message' : 'product addded to cart'})
    except Exception as e:
        print(f"error adding to cart: {e}")
        return jsonify({'error': 'internal server error'}), 5000

@app.route('/cart/items/<cart_id>', methods=['GET'], strict_slashes=False)
def get_cart_items(cart_id):
    try:
        #cart_id = request.args.get('cart_id')  # Get cart_id from query parameter
        # Check for valid cart_id
        if not cart_id:
            return jsonify({'error': 'Missing cart_id'}), 400
        # Retrieve cart and its items
        cart = storage.get(Cart, cart_id)
        if not cart:
            return jsonify({'message': 'Cart not found'}), 404
        # Convert cart items to a list of dictionaries
        cart_items = [{
                      'product_id': item.product_id,
                      'quantity': item.quantity,
                      'id': item.id,
                      'url': item.url
                     } for item in cart.items]
        return jsonify({'cart_items': cart_items}), 200
    except Exception as e:
        print(f"Error retrieving cart items: {e}")
        return jsonify({'error': 'Internal server error'}), 500



@app.route('/cart/items/<cart_id>/<product_id>', methods=['DELETE'], strict_slashes=False)
def delete_cart_item(cart_id, product_id):
    try:
        cart_items = storage.all(CartItem).values()
        for cart_item in cart_items:
            if cart_item.cart_id == cart_id:
                if cart_item.product_id == product_id:
                    storage.delete(cart_item)
                    storage.save()
                    return jsonify({'message': 'Cart item deleted'}), 200

        # Check for valid item_id
        return jsonify({'error': 'Cart item not found'}), 404
                      
    except Exception as e:
        print(f"Error deleting cart item: {e}")
        return jsonify({'error': 'Internal server error'}), 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

