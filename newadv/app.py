# app.py
from flask import Flask, render_template, request
#<F11>from data import images_data  # Import the image data from data.py
from data import *

app = Flask(__name__)

@app.route('/')  # Define the route for the homepage
def index():
    # Pass the imported image data to the template
    return render_template('landpage.html', images=images_data)

@app.route('/cloth')
def cloth():
    # Pagination parameters
    page = int(request.args.get('page', 1))  # Default to page 1 if not specified
    per_page = 5  # Number of products per page

    # Fetch paginated products from Shopify
    products = get_shopify_products(page=page, per_page=per_page)

    # Generate images for each product based on its type
    product_images = {}
    for product in products:
        product_images[product['type']] = generate_images_for_product(product['type'])

    # Pagination logic
    total_products = 15  # You can modify this based on your total product count
    total_pages = (total_products // per_page) + (1 if total_products % per_page > 0 else 0)
    
    return ('cloth.html', products==products, product_images==product_images, page==page, total_pages==total_pages)


if __name__ == '__main__':
    app.run(debug=True)

