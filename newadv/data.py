import shopify
import requests
#from config import SHOPIFY_API_KEY, SHOPIFY_API_PASSWORD, SHOPIFY_STORE_NAME

def authenticate_shopify():
    """Authenticate and set the Shopify store session."""
    SHOP_NAME = 'stringlord'
    API_KEY = 'd7cc4ec8fef8d773ca288894ca428502'
    API_PASSWORD = '21dbaf914e610bc34bd4d2964123f9e5'
    shop_url = f"https://{API_KEY}:{API_PASSWORD}@{SHOP_NAME}.myshopify.com"

    shopify.ShopifyResource.set_site(shop_url)

def get_shopify_products(page=1, per_page=5):
    """Fetch products from Shopify with pagination and return product details including image URLs."""
    authenticate_shopify()

    # Fetch products with pagination
    products = shopify.Product.find(limit=per_page, page=page)
    
    product_list = []
    for product in products:
        product_data = {
            'name': product.title,
            'id': product.id,
            'type': product.product_type,  # Product type (T-shirt, Shoes, etc.)
            'price': product.variants[0].price,  # Assuming first variant for price
            'images': [image.src for image in product.images]  # Extract actual image URLs
        }
        product_list.append(product_data)

    return product_list

def generate_images_for_product(product_type):
    """Generate image URLs for products based on their type."""
    # Example: Generate some placeholder image URLs (this part is typically for non-Shopify products)
    images = []
    
    if product_type == 'T-shirt':
        images = [f'https://via.placeholder.com/300x200?text=T-shirt+{i}' for i in range(1, 16)]
    elif product_type == 'Blazers':
        images = [f'https://via.placeholder.com/300x200?text=Blazer+{i}' for i in range(1, 16)]
    elif product_type == 'Gowns':
        images = [f'https://via.placeholder.com/300x200?text=Gown+{i}' for i in range(1, 16)]
    elif product_type == 'Shoes':
        images = [f'https://via.placeholder.com/300x200?text=Shoes+{i}' for i in range(1, 16)]
    
    return images

# Example usage of getting Shopify products with images
if __name__ == "__main__":
    products = get_shopify_products(page=1, per_page=5)
    for product in products:
        print(f"Product: {product['name']}, Images: {product['images']}")

