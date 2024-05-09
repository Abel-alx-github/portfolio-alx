


async function fetchCartData() {
  try {
     const cartId = localStorage.getItem('cartId');
     const response = await fetch(`http://localhost:5000/cart/items/${cartId}`, {
           method: 'GET', // Adjust the endpoint URL as needed
           headers: {
                    'Content-Type': 'application/json' // Optional for JSON data
	        }
	  });

          if (response.ok) {
             const data = await response.json();
	     const cartItems = data.cart_items || [];
	     console.log(cartItems); 
	     // this is my custom logic

             updateCartUI(cartItems); // Update UI with fetched data
          } else {
            console.error('Error fetching cart data:', response.statusText);
            // Handle errors gracefully, e.g., display an error message to the user
	    }
    } catch (error) {
        console.error('Error:', error);
        // Handle unexpected errors
    }
}





async function product_detail(url, callback) {
  try {
      const response = await fetch(url, {
            method: 'GET', // Adjust the endpoint URL as needed
            headers: { 'Content-Type': 'application/json' } // Optional for JSON data
       });
       if (response.ok) {
          const data = await response.json();
	  console.log('console.log', data);
	  const product = data.products[0]; // Assuming the first element is the product
	  callback(product);
     } else {
          console.error('Error fetching product details:', response.statusText);
         return {}; // Example: return an empty object to avoid undefined errors
							          }
 } catch (error) {
       console.error('Error:', error);
       // Handle unexpected errors
      return {}; 
   }
}



async function deleteCartItem(product_id) {
  try {
     console.log("product_id", product_id)
     const cartId = localStorage.getItem('cartId');
     const url = `http://localhost:5000/cart/items/${cartId}/${product_id}/`;
     console.log("url", url)
     const response = await fetch(url, {
           method: 'DELETE', 
           headers: {
                    'Content-Type': 'application/json'
	        }
	  });

          if (response.ok) {
             const data = await response.json();
	     const cartItems = data.cart_items || [];
	     console.log(cartItems); 
	   
	fetchCartData();
          } else {
            console.error('Error fetching cart data:is not ok', response.statusText);
            // Handle errors gracefully, e.g., display an error message to the user
	    }
    } catch (error) {
        console.error('Error:', error);
        // Handle unexpected errors
    }
}



async function updateCartUI(cartItems) {
  const cartItemsContainer = document.getElementById('cart-items-container');

  cartItemsContainer.innerHTML = '';
  let subtotalPrice = 0; // Accumulate subtotal price
  
const shippingCost = 10; //

  cartItems.forEach(async cartItem => {
       product_detail(cartItem.url, function(productData) {
	        if (productData) {

		        subtotalPrice += cartItem.quantity * productData.price; // Calculate subtotal per item
			const grandTotal = subtotalPrice + shippingCost; 
			const subtotalElement = document.getElementById('cart-subtotal');
			const grandTotalElement = document.getElementById('cart-grand-total');
			const shippingElement = document.getElementById('shipping');
			
			shippingElement.textContent = '$10';
			subtotalElement.textContent = `$${subtotalPrice.toFixed(2)}`;
			grandTotalElement.textContent = `$${grandTotal.toFixed(2)}`;
                        
			const tableRow = document.createElement('tr');
        	        // Create table cells based on cart item properties
		        const deleteCell = document.createElement('td');
		        const imageCell = document.createElement('td');
		        const productCell = document.createElement('td');
		        const priceCell = document.createElement('td');
		        const quantityCell = document.createElement('td');
		        const totalCell = document.createElement('td');
		        
			// Example content for each cell (use productData from the callback)
     deleteCell.innerHTML = `<a href="#" class="delete-cart-item" data-product-id="${productData.id}" onclick="deleteCartItem('${productData.id}')"><i class="fas fa-trash"></i></a>`;
		        imageCell.innerHTML = `<img src="${productData.image_url}" alt="">`;
		        productCell.innerHTML = `<h5>${productData.name}</h5>`;
		        priceCell.innerHTML = `<h5>$${productData.price}</h5>`;
		        quantityCell.innerHTML = `<input type="number" class="w-25 pl-1" value="${cartItem.quantity}">`;
        	        totalCell.innerHTML = `<h5>$${(productData.price * cartItem.quantity).toFixed(2)}</h5>`; // Calculate total

	 	        // Append cells to the table row and container
		        tableRow.appendChild(deleteCell);
		        tableRow.appendChild(imageCell);
		        tableRow.appendChild(productCell);
		        tableRow.appendChild(priceCell);
		        tableRow.appendChild(quantityCell);
		        tableRow.appendChild(totalCell);
	
			cartItemsContainer.appendChild(tableRow);
		      }
		    });

	  });

}







/**
  const deleteCartItemButtons = document.querySelectorAll('.delete-cart-item');

deleteCartItemButtons.forEach(button => {
		  button.addEventListener('click', function(event) {
				      event.preventDefault(); // Prevent default anchor tag behavior

				          const productId = this.dataset.productId;
					      deleteCartItem(productId);
					        });
		  });



**/




fetchCartData()
