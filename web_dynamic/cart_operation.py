#!/user/bin/python3

from models import storage

from models.cart import Cart


def add_to_cart(**kw):
    cart_item = Cart(**kw)
    storage.new(cart_item)
    storage.save()
    print('item added to db successfully')
        
def get_cart_item(user_id:str):
    cart_items = storage.all(Cart).values()
    items = []
    for item in cart_items:
        if item.user_id == user_id:
            items.append(item)
    return items


def delete_cart_item(cart_id: str):
    cart = storage.get(Cart, cart_id)

    storage.delete(cart)
    storage.save()
    print('item is deleted successfully')
    
def update_cart_item(cart_id: str, quantity: int):
    cart = storage.get(Cart, cart_id)
    if cart:
        cart.quantity = quantity
        storage.save()
        print('updated')

        



kw = {
      "id": 'f',
      "user_id": "1",
      "product_id" : "fd666967-6938-4550-965d-e3c5d4447d08",
      "quantity": 2,
      "price": 100}

#add_to_cart(**kw)
#delete_cart_item("6b7613d1-a748-4ca7-907b-f9f0890a8c47")
#id = 'f'
#update_cart_item(id, 10)

#cart = get_cart_item('1')
#for i in cart:
#    print(i.values())
