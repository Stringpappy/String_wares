from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True)

