/*
fetch from api clothes and display
*/

async function getProducts() {
  try {
      const response = await fetch("http://localhost:5000/clothes"); // Replace with your API endpoint
      if (!response.ok) {
         throw new Error(`API request failed with status ${response.status}`);
     }
       const data = await response.json();
        return data.products; // Assuming the API response has a "products" property
        //return data
  } catch (error) {
      console.error("Error fetching products:", error);
    // Handle error gracefully, e.g., display an error message to the user
      return []; // Return an empty array in case of error
  }
}

async function displayProducts() {
	  const products = await getProducts();
	    const productContainer = document.getElementById("root");
	      productContainer.innerHTML = ""; // Clear existing content

	        products.forEach((product) => {
         	    const productElement = createProductElement(product);
	             productContainer.appendChild(productElement);
		  });
}

function createProductElement(product) {
	  const element = document.createElement("div");
	    element.classList.add("products", "text-center", "col-lg-3", "col-md-4", "col-12");

	      // Add product details (image, name, price, etc.) based on your product data structure
	      element.innerHTML = `
		          <img class="f-img img-fluid mb-3" src="${product.image_url}" alt="">
			  <div class="stars">
			  <i class="fa-solid fa-star"></i>
			  <i class="fa-solid fa-star"></i>
			  <i class="fa-solid fa-star"></i>
			  <i class="fa-solid fa-star"></i>
			  <i class="fa-solid fa-star"></i>
		 </div>
		 <h5 class="p-name">${product.name}</h5>
		 <h3 class="p-price">$${product.price}</h3>
		 <button class="add2cart" type="button" data-product-id="${product.id}">Buy Now</button>`; // Add functionality for "Buy Now" button
	     
	      // Implement event listener for a cleaner approach
	        element.querySelector('.add2cart').addEventListener('click', function() {
				    addToCart(product.id, product.url); // Call your cart functionality with product ID
				      });

	        return element;
}

/* addToCart */

//import { v4 as uuidv4 } from 'uuid';
//const { v4: uuidv4 } = require('uuid');
//const uuidv4 = window.uuidv4;
function generateRandomId() {
	  return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 5);
}

function getCartIdFromLocalStorage() {
  try {
     const storedCartId = localStorage.getItem('cartId');
     if (storedCartId) {
        return storedCartId;
     } else {
       const newCartId = generateRandomId();
       localStorage.setItem('cartId', newCartId);
       return newCartId;
     }
   } catch (error) {
     console.error('Error retrieving cartId from LocalStorage:', error);
    // Handle potential errors (e.g., quota exceeded) and consider alternative approaches
    return null; // Or return a default value or handle in calling function
    }
}




async function addToCart(productId, url) {
  try {
      const cartId = getCartIdFromLocalStorage();
      const response = await fetch("http://localhost:5000/cart/add", {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cartId, productId, url}),
	    });

          if (!response.ok) {
             throw new Error(`Failed to add product to cart: ${response.statusText}`);
	    }

         const updatedCart = await response.json();  // Assuming response contains updated cart data
         console.log('Product added to cart:', updatedCart);

         // Update cart UI dynamically (optional)
        // updateCartUI(updatedCart);
        } catch (error) {
	    console.error('Error adding product to cart:', error);
            // Handle errors (e.g., display error message to user)
       }
}



displayProducts(); // Call the function to fetch and display products on page load




