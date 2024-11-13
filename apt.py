from flask import Flask, render_template, request, redirect, url_for
from math import ceil

app = Flask(__name__)

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_to_cart(self, item, quantity=1):
        """Add an item to the cart with a specified quantity."""
        if item in self.cart:
            self.cart[item] += quantity
        else:
            self.cart[item] = quantity

    def remove_from_cart(self, item):
        """Remove an item from the cart."""
        if item in self.cart:
            del self.cart[item]

    def update_quantity(self, item, quantity):
        """Update the quantity of an item in the cart."""
        if item in self.cart:
            if quantity <= 0:
                self.remove_from_cart(item)
            else:
                self.cart[item] = quantity

    def view_cart(self):
        """Return the current items in the cart."""
        return self.cart

# Initialize the shopping cart
cart = ShoppingCart()

# Sample list of image paths (could be fetched from a database or filesystem)
images = ['images/g.jpg', 'images/g2.jpg', 'images/g3.jpg', 'images/g4.jpg', 'images/g5.jpg',
          'images/g6.jpg', 'images/g7.jpg', 'images/g8.jpg', 'images/g9.jpg', 'images/g10.jpg',
          'images/g11.jpg', 'images/g12.jpg', 'images/g13.jpg', 'images/g14.jpg', 'images/g15.jpg',
          'images/g16.jpg', 'images/g17.jpg', 'images/g18.jpg', 'images/g19.jpg', 'images/g20.jpg',
          'images/g21.jpg', 'images/g22.jpg', 'images/g23.jpg', 'images/g24.jpg', 'images/g25.jpg',
          'images/g26.jpg', 'images/g27.jpg', 'images/g28.jpg', 'images/g29.jpg', 'images/g30jpg',
          'images/g31.jpg', 'images/g32.jpg', 'images/g33.jpg', 'images/g34.jpg', 'images/g35.jpg',
          'images/g36.jpg', 'images/g37.jpg', 'images/g38.jpg', 'images/g38.jpg', 'images/g40.jpg',
          'images/g41.jpg', 'images/g42.jpg', 'images/g43.jpg', 'images/g44.jpg', 'images/g45.jpg',
          'images/g46.jpg', 'images/g47.jpg', 'images/g.48jpg', 'images/g49.jpg', 'images/g50.jpg']

@app.route('/cloth')
def grid_view():
    # Pagination logic
    per_page = 25  # Number of items per page (5x5 grid)
    page = request.args.get('page', 1, type=int)  # Get the current page, default is 1

    # Calculate the start and end index for the current page
    start = (page - 1) * per_page
    end = start + per_page

    # Paginate the images list
    paginated_images = images[start:end]

    # Calculate total pages
    total_pages = ceil(len(images) / per_page)

    return render_template('cloth.html', images=paginated_images, page=page, total_pages=total_pages)



@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'add' in request.form:
            item = request.form.get('item', 'Stylish Wristwatch')  # Default item
            quantity = int(request.form.get('quantity', 1))
            cart.add_to_cart(item, quantity)
        elif 'remove' in request.form:
            item = request.form.get('item')
            cart.remove_from_cart(item)
        elif 'update' in request.form:
            item = request.form.get('item')
            quantity = int(request.form.get('quantity'))
            cart.update_quantity(item, quantity)
        return redirect(url_for('index'))  # Redirect to the same page after processing

    return render_template('index.html', cart=cart.view_cart())


@app.route('/')
def landingpage():
    
        return render_template('homepage.html')

@app.route('/cartlist')
def cartlist():
    """Render the cart page displaying the current items in the cart."""
    return render_template('cart_list.html', cart=cart.view_cart())


@app.route("/cloth")
def clothe():
    return render_template('cloth.html', images=paginated_images, page=page, total_pages=total_pages)

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)