/**const products_ = [
  {
    id: 12,
    image: 'image/clothes/ja0.jpg',
    title: 'womens-boho',
    price: 80
  },

  {
    id: 0,
    image: '/image/clothes/cl0.jpg',
    title: 'beauty',
    price: 200
  },
  {
    id: 1,
    image: 'image/clothes/cl1.jpg',
    title: 'buddha',
    price: 30
  },

  {
    id: 2,
    image: 'image/clothes/cl2.jpg',
    title: 'dainity',
    price: 40
  },

  {
    id: 3,
    image: 'image/clothes/cl3.jpg',
    title: 'cloth..',
    price: 59
  },

  {
    id: 4,
    image: 'image/clothes/cl4.jpg',
    title: 'cloth..',
    price: 70
  },

  {
    id: 5,
    image: 'image/clothes/cl5.jpg',
    title: 'cloth..',
    price: 40
  },

  {
    id: 6,
    image: 'image/clothes/cl6.jpg',
    title: 'cloth..',
    price: 80
  },

  // {
  //     id: 7,
  //     image: 'image/clothes/cl7.jpg',
  //     title: 'cloth..',
  //     price: 70,
  // },

  {
    id: 8,
    image: 'image/clothes/cl8.jpg',
    title: 'cloth..',
    price: 100
  },
  {
    id: 9,
    image: 'image/clothes/cl9.jpg',
    title: 'pexels-lum3n',
    price: 80
  },
  {
    id: 10,
    image: 'image/clothes/cl10.jpg',
    title: 'cloth..',
    price: 200
  }
  // {
  //     id: 11,
  //     image: 'image/clothes/cl11.jpg',
  //     title: 'cloth..',
  //     price: 790,
  // },

];
*/


/*
async function getProducts() {
  try {
     const response = await fetch('http://localhost:5000/clothes'); // Assuming your Flask app runs on port 5000
     if (!response.ok) {
        throw new Error(`Error fetching products: ${response.status}`);
   }
     const data = await response.json();
     products = data.products;
     for(const p of products) {
	return (
        `<div class="products text-center col-lg-3 col-md-4 col-12">
            <img class="f-img img-fluid mb-3" src=${p.image_url}>

            <div class="stars">
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
            </div>
            <h5 class="p-name">${p.name}</h5>
            <h3 class="p-price">${p.price}.00</h3>` +

            `<button onclick='addtocart("+(i++)+")' type="button">Buy Now</button>
       </div>
      `
     }

      // This will log the response data (products)
		          // Use the data object (containing the 'products' list) in your JavaScript code
   } catch (error) {
       console.error('Error:', error);
   }
}

getProducts();
data = fetch("http://localhost:5000/clothes");
const categories = [...new Set(data.ptroducts.map((item)=>
    {return item}))]
    let i=0;
document.getElementById('root').innerHTML = categories.map((item)=>
{
    let {image_url, name, price} = item;
    return (
        `<div class="products text-center col-lg-3 col-md-4 col-12">
            <img class="f-img img-fluid mb-3" src=${image_url}>

            <div class="stars">
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
            </div>
            <h5 class="p-name">${name}</h5>
            <h3 class="p-price">${price}.00</h3>` +

            `<button onclick='addtocart("+(i++)+")' type="button">Buy Now</button>
    </div>
    `
    )
}).join('')

*/

async function getProducts () {
  try {
    const response = await fetch('http://localhost:5000/clothes'); // Assuming your Flask app runs on port 5000
    if (!response.ok) {
      throw new Error(`Error fetching products: ${response.status}`);
    }
    const data = await response.json();
    const productsContainer = document.getElementById('root');
    productsContainer.innerHTML = ''; // Clear existing content
    for (const product of data.products) {
      const productElement = document.createElement('div');
      productElement.classList.add('products', 'text-center', 'col-lg-3', 'col-md-4', 'col-12'); // Add CSS classes
      const productImage = document.createElement('img');
      productImage.classList.add('f-img', 'img-fluid', 'mb-3');
      productImage.src = product.image_url; // Set image source
      const productDetails = document.createElement('div');
      const starsElement = document.createElement('div');
      starsElement.classList.add('stars');
      for (let i = 0; i < 5; i++) {
        const star = document.createElement('i');
        star.classList.add('fa-solid', 'fa-star'); // Assuming Font Awesome for stars
        starsElement.appendChild(star);
      }
      const productName = document.createElement('h5');
      productName.classList.add('p-name');
      productName.textContent = product.name;
      const productPrice = document.createElement('h3');
      productPrice.classList.add('p-price');
      productPrice.textContent = `$${product.price.toFixed(2)}`; // Format price with two decimal places
      const buyButton = document.createElement('button');
      buyButton.type = 'button';
      buyButton.classList.add('btn', 'btn-primary'); // Assuming Bootstrap for button styling
      buyButton.textContent = 'Buy Now';
      buyButton.addEventListener('click', () => {
        // Handle "Buy Now" button click (implement your cart logic here)
        console.log(`Adding product "${product.name}" to cart (implementation required)`);
        productDetails.appendChild(starsElement);
        productDetails.appendChild(productName);
        productDetails.appendChild(productPrice);
        productDetails.appendChild(buyButton);
        productElement.appendChild(productImage);
        productElement.appendChild(productDetails);
        productsContainer.appendChild(productElement);
      });
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

/*

data.fetch("http://localhost:5000/clothes")
  .then(response => response.json())
  .then(data => {
    const categories = [...new Set(data.products.map(item => item))]; // Optional based on your data
    let i = 0;
    document.getElementById('root').innerHTML = categories.map(item => {
      let { image_url, name, price } = item;
      return (
         `<div class="products text-center col-lg-3 col-md-4 col-12">
         <img class="f-img img-fluid mb-3" src=${image_url}>
         <div class="stars">
         <i class="fa-solid fa-star"></i>
         <i class="fa-solid fa-star"></i>
         <i class="fa-solid fa-star"></i>
         <i class="fa-solid fa-star"></i>
         <i class="fa-solid fa-star"></i>
        </div>
         <h5 class="p-name">${name}</h5>
         <h3 class="p-price">${price}.00</h2>
         <button onclick="addToCart(${i++})" type="button">Buy Now</button>
         </div>`
       );
    }).join('');
 });

 */

var cart = [];

function addtocart(a) {
    cart.push({...categories[a]});
    displaycart();
}

function displaycart() {
    let j = 0, total = 0;
    document.getElementById('count').innerHTML = cart.length;
    if (cart.length == 0) {
        document.getElementById('cartItem').innerHTML = 'Your cart is empty';
        document.getElementById('total').innerHTML = "$ "+0+".00";
    } else {
        document.getElementById('cartItem').innerHTML = cart.map((item) => {
            let {image, title, price} = item;
            total = total + price;
            document.getElementById('total').innerHTML = '$ '+total+'.00';
            return (
                `<div class='cart-item'>
                    <div class='row-img'>
                        <img class='rowimg' src=${image}>
                    </div>
                    <p style='font-size:12px;'>${title}</p>
                    <h2 style='font-size:15px;'>${price}.00</h2>`+
                "<i class='fa-solid fa-trash' onclick='delElement("+(j++)+")'></i></div>"
            );
        }).join('');
    }
}

function delElement(a) {
    cart.splice(a, 1);
    displaycart();
}


