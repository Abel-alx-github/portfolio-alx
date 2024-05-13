#!/usr/bin/python3
""" module contain flask application"""

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

# release database resource when the session end
@app.teardown_appcontext
def close_db(error):
    storage.close()

# render home page template
@app.route('/index.html')
def home():
    return render_template("index.html")

# render clothes page template
@app.route('/clothes.html')
def clothe():
    return render_template("clothes.html")

# return clothes product serve as api end point page template
@app.route('/clothes', methods=['GET'], strict_slashes=False)
def get_clothes():
    products = storage.all(Product).values()
    product_list = [
        {"id": p.id, "name": p.name, "price": p.price, "image_url": p.image_url, "url": p.url + p.id} for p in products if p.category_id == "1" ]
    return jsonify({'products': product_list})
    
# return shoes products serve as api end points    
@app.route('/shoes', methods=['GET'], strict_slashes=False)
def get_shoes():
    products = storage.all(Product).values()
    product_list = [
        {"id": p.id, "name": p.name, "price": p.price, "description": p.description, "image_url": p.image_url, "url": p.url + p.id} for p in products if p.category_id == "2" ]
    return jsonify({'products': product_list})
   
# return watches products serve as api end points 
@app.route('/watches', methods=['GET'], strict_slashes=False)
def get_watches():
    products = storage.all(Product).values()
    product_list = [
        {"id": p.id, "name": p.name, "price": p.price, "description": p.description, "image_url": p.image_url, "url": p.url + p.id} for p in products if p.category_id == "3" ]
    return jsonify({'products': product_list})

# return accessories products serve as api end points 
@app.route('/accessories', methods=['GET'], strict_slashes=False)
def get_accessories():
    products = storage.all(Product).values()
    product_list = [
        {"id": p.id, "name": p.name, "price": p.price, "description": p.description, "image_url": p.image_url, "url": p.url + p.id} for p in products if p.category_id == "4" ]
    return jsonify({'products': product_list})

# return a product by its id, serve as api end points 
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

# add items(product) to cart, serve as api end points 
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

# return cart items(products) using cart_id, serve as api end points 
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


# delete item from cart using cart_id and product_id, serve as api end points 
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
    # run the flask application on all ip at port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)

