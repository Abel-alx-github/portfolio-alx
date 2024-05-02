const fetch = require('node-fetch'); // Assuming you're using Node.js v18 or above (built-in fetch)
let data = ""
async function getProducts() {
  try {
     const response = await fetch('http://localhost:5000/clothes'); // Assuming your Flask app runs on port 5000
     if (!response.ok) {
        throw new Error(`Error fetching products: ${response.status}`);
    }
      data = await response.json();
      console.log(data.products); // This will log the response data (products)
                        // Use the data object (containing the 'products' list) in your JavaScript code
    } catch (error) {
        console.error('Error:', error);
    }
 }
getProducts();

