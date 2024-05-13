# FreButiqe -- E-commerce Website --

## FreButiqe - Your One-Stop Shop for Stylish Women's Fashion - Project Overview

<p>FreButiqe is a curated online boutique offering a delightful selection of women's fashion that empowers you to express your unique style. We understand that every woman is special, and our goal is to provide you with high-quality, on-trend pieces that make you feel confident and beautiful. </p>

- Authour: Abel Tibeso (https://linkedin.com/in/abel-tibeso/)
  
![image](https://github.com/Abel-alx-github/portfolio-alx/assets/138770113/6d6a0d11-d89d-47f8-a9ac-6dcbec31829f)

## Installation

Here's how to set up your development environment and install the necessary dependencies to run the FreButiqe e-commerce website:

### Prerequisites:

**Operating System:** Any operating system (Windows, macOS, Linux) will work as long as you can install the required dependencies.

**Python:** Download and install Python 3 (https://www.python.org/downloads/). Make sure to add Python to your system's PATH environment variable during installation.
Steps:

1. Clone the Repository:
   ``` clone
      Bash
      git clone https://github.com/Abel-alx-github/portfolio-alx.git

2. Navigate to the Project Directory:
   ``` cd to folder
       cd portfolio-alx

3. Create a Virtual Environment (Optional but Recommended):

   A virtual environment is a self-contained Python environment that isolates dependencies for this project from 
   other projects on your system. It's highly recommended to use a virtual environment for better project 
   management. Here's how to create one using venv:
   ``` create venv
       python -m venv venv  # Replace 'venv' with your desired virtual environment name

       Now, activate the virtual environment:

       # Windows
       venv\Scripts\activate.bat

       # macOS/Linux
       source venv/bin/activate
   ```
 4. Install Dependencies:

   ``` 
      pip install -r requirements.txt
  ```

## Usage
   This section guides you through navigating and interacting with the FreButiqe e-commerce website.

### Browsing Products:

**Homepage:** The homepage showcases featured products, categories, and promotions.

**Categories:** Explore products by category (e.g., Clothes, Shoes, Watches, Accessories) using the navigation bar or menu.

**Product Listing Pages:** Each category page displays a list of products with thumbnail images, names, and prices. 

**Product Details Pages:** Clicking on a product takes you to its dedicated page with a detailed description, high-quality images, size and color options, and customer reviews (if available).

[Start Browsing Now](HTTP://fre.abeldev.tech)

### Adding Items to Cart:

   On a product detail page, choose your desired size and color (if applicable).
   Click the "Add to Cart" button.
   The item will be added to your shopping cart. A notification might appear or update the cart icon in the 
   navigation bar.
   You can continue browsing or navigate directly to your cart.
   Managing Your Cart:

   Access your cart through the cart icon in the navigation bar.
   Here, you can view the items in your cart, their quantities, adjust quantities using up/down buttons or by 
   entering a value, and remove items entirely.
   
   Update the cart quantities as needed.

   [Start Browsing Now](HTTP://fre.abeldev.tech)

## Technologies Used

### Front-End:
  **HTML (Markup Language):** Provides the core structure and content of the website.
  
  **CSS (Bootstrap):** Handles styling and layout, ensuring responsiveness across different devices.
  
  **JavaScrip:** Enables dynamic data fetching and manipulation, enhancing user interaction.

### Back-End:
  **Python Flask:** A lightweight web framework for creating robust and scalable APIs.
  
  **SQLAlchemy:** An ORM (Object-Relational Mapper) that simplifies database interaction and data model management.
 
  **MySQL:** A widely used relational database for storing product data, categories, carts, cart items, and user information.
  
### Deployment:
  
  **Operating System:** Choose a stable and reliable operating system like Ubuntu Server for production deployment.
  
  **Web Server:** Deploy the application using a high-performance web server like Nginx.
  
  **WSGI Server:** A WSGI (Web Server Gateway Interface) server like Gunicorn is needed to connect Flask with Nginx.

## project structure visualized as a tree:

    web_dynamic/
    ├── __init__.py
    ├── app.py 
    ├── cart_operation.py
    ├── models/
    │   ├── __init__.py
    │   ├── base_model.py
    │   ├── cart.py
    │   ├── cart_item.py
    │   ├── category.py
    │   ├── engine/
    │   │   └── db_storage.py
    │   ├── product.py
    │   └── user.py
    ├── requirements.txt
    ├── sample_product.py
    ├── static/
    │   ├── image/
    │   ├── img/
    │   ├── js/
    │   └── style/
    └── templates/
        ├── accessories.html
        ├── clothes.html
        ├── contact.html
        ├── index.html
        ├── old.html
        ├── product-detail.html
        ├── shoes.html
        └── wathes.html

## Contributing
   We welcome contributions from the community to help make FreButiqe even better! Here's how you can get involved:

1. **Reporting Issues:**

   If you encounter any bugs or unexpected behavior while using FreButiqe, please create an issue on the project's 
   GitHub repository (https://github.com/Abel-alx-github/portfolio-alx.git).

   Provide clear and concise descriptions of the issue, including steps to reproduce it if possible. Screenshots or 
   error messages can be helpful for further debugging.

2. **Suggesting Enhancements:**

   Do you have ideas for new features or improvements to FreButiqe? Feel free to create an issue on GitHub 
   outlining your suggestion.
   
   Clearly explain the functionality you propose and its potential benefits for users.
   Be open to discussing alternative approaches and feasibility with the development team.

3. **Submitting Pull Requests:**

   If you're comfortable with code contributions, you can fork the project repository on GitHub, make your changes, 
   and submit a pull request.
   Ensure your code adheres to the project's coding style and formatting guidelines
   
   Write clear and concise commit messages that describe your changes.
   Consider creating unit tests for your code changes to ensure quality and maintainability.

**Before Contributing:**

   Please take some time to familiarize yourself with the project structure, codebase, and existing documentation.
   It's recommended to discuss your contributions (enhancements or pull requests) with the project maintainers 
   beforehand to avoid conflicts or duplication of effort.
 **Additional Resources:**

   Consider reviewing existing code style guides.
   Familiarize yourself with Git workflows for effective version control and collaboration.
   
   We appreciate your interest in contributing to FreButiqe!


## Related Projects
   Here are some open-source e-commerce platforms or projects that might be interesting to explore alongside F 
   FreButiqe:

   - **Django E-Commerce:** A well-established Django-based e-commerce framework offering a solid foundation for building 
                   online stores (https://djangopackages.org/grids/g/ecommerce/).
   - **Saleor:** A GraphQL-first e-commerce platform with a focus on flexibility and scalability (https://saleor.io/).
               Sylius: A Symfony-based e-commerce framework known for its modularity and customization options 
               (https://sylius.com/).
   - **OpenCart:** A user-friendly open-source e-commerce platform with a wide range of extensions and themes 
                 available (https://www.opencart.com/).
   - **PrestaShop:** Another popular open-source e-commerce solution with a large community and extensive features 
                   (https://prestashop.com/).
   
  
## License
   FreButiqe is licensed under the [MIT License](/LICENSE). 
    
   **This license grants you the freedom to:**
    
   Use the code: Freely use, modify, and distribute the code in your own projects, commercial or non-commercial.
   
   Modify the code: Adapt and change the code to suit your specific needs.
   
   Redistribute the code: Share the code with others, either in its original form or modified versions.

   Copyright (c) 2024 Abel Tibeso
