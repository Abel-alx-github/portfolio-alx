const product = [
    {
        id: 12,
        image: 'image/clothes/ja0.jpg',
        title: 'womens-boho',
        price: 80,
    }, 

   
    {
        id: 0,
        image: '/image/clothes/cl0.jpg',
        title: 'beauty',
        price: 200,
    },
    {
        id: 1,
        image: 'image/clothes/cl1.jpg',
        title: 'buddha',
        price: 30,
    },
    
    {
        id: 2,
        image: 'image/clothes/cl2.jpg',
        title: 'dainity',
        price: 40,
    },
    
    {
        id: 3,
        image: 'image/clothes/cl3.jpg',
        title: 'cloth..',
        price: 59,
    },

    {
        id: 4,
        image: 'image/clothes/cl4.jpg',
        title: 'cloth..',
        price: 70,
    },

    {
        id: 5,
        image: 'image/clothes/cl5.jpg',
        title: 'cloth..',
        price: 40,
    },

    {
        id : 6,
        image: 'image/clothes/cl6.jpg',
        title: 'cloth..',
        price: 80,
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
        price: 100,
    },
    {
        id: 9,
        image: 'image/clothes/cl9.jpg',
        title: 'pexels-lum3n',
        price: 80,
    },
    {
        id: 10,
        image: 'image/clothes/cl10.jpg',
        title: 'cloth..',
        price: 200,
    },
    // {
    //     id: 11,
    //     image: 'image/clothes/cl11.jpg',
    //     title: 'cloth..',
    //     price: 790,
    // },

    
       
];

const categories = [...new Set(product.map((item)=>
    {return item}))]
    let i=0;
document.getElementById('root').innerHTML = categories.map((item)=> 
{
    let {image, title, price} = item;
    return (
        `<div class="products text-center col-lg-3 col-md-4 col-12">
            <img class="f-img img-fluid mb-3" src=${image}>

            <div class="stars">
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
                <i class="fa-solid fa-star"></i>
            </div>
            <h5 class="p-name">${title}</h5>
            <h3 class="p-price">${price}.00</h3>` +

            `<button onclick='addtocart("+(i++)+")' type="button">Buy Now</button>
    </div>  
    `
    ) 
}).join('')




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


