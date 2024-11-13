#!/usr/bin/env python3
from flask import Flask, url_for, request, render_template, jsonify
import requests  # Import the requests module to handle HTTP requests
from item import *  # Assuming item is some other part of your code (not shown here)
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

SHOP_NAME = 'Stringlord'  # Replace with your Shopify store name
API_KEY = 'd7cc4ec8fef8d773ca288894ca428502'  # Replace with your API key
API_PASSWORD = '21dbaf914e610bc34bd4d2964123f9e5' 
#SHOPIFY_API_URL = f'https://{API_KEY}:{API_PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/2024-01/products.json'
SHOPIFY_API_URL = f'https://{SHOP_NAME}.myshopify.com/admin/api/2024-01/products.json'

# Categories that you want to fetch
CATEGORY_LIST = [
    'Clothing', 'Blouses', 'trousers', 'caps', 'underwear', 'tie', 'shorts', 
    'blankets', 'native wares', 'sweaters', 'hoodie'
]

# Function to get products from Shopify store
def fetch_shopify_products():
    try:
        # Use requests.get instead of request.get
        response = requests.get(SHOPIFY_API_URL, auth=HTTPBasicAuth(API_KEY, API_PASSWORD) )  # Note the use of 'requests' here
        response.raise_for_status()  # Raises an exception for 4xx/5xx responses
        print(response.json())  # optional,Debug: log the response content
        return response.json()['products']
    except requests.exceptions.RequestException as e:  # Handle exceptions correctly
        print(f"Error fetching Shopify products: {e}")
        return []

# Function to categorize products
def categorize_products(products):
    categorized = {category: [] for category in CATEGORY_LIST}
    
    for product in products:
        title = product.get('title', '').lower()
        image_url = product.get('images', [{}])[0].get('src', '')
        
        # Check if the product title contains any category keyword
        for category in CATEGORY_LIST:
            if category in title:
                categorized[category].append({
                    'name': product.get('title'),
                    'image': image_url,
                    'link': f'https://{SHOP_NAME}.myshopify.com/products/{product["handle"]}'
                })
                break
    
    return categorized


@app.route('/')
def landpage():
    return render_template('landpage.html', images=images_data)


@app.route('/cloth')
def cloth():
    products = fetch_shopify_products()
    categorized_products = categorize_products(products)
    return render_template('cloth.html', categorized_products=categorized_products)
    
# Returns the categories in JSON format
@app.route('/api/products')
def api_products():
    products = fetch_shopify_products()
    categorized_products = categorize_products(products)
    return jsonify(categorized_products)

@app.route('/jewelries')
def jewelries():
    return render_template('jewelries.html')


if __name__ == "__main__":
    app.run(debug=True)


