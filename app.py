from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Static list of products
products = [
    {
        'id': 1,
        'name': 'Product 1',
        'description': 'Description of product 1',
        'price': 10.99
    },
    {
        'id': 2,
        'name': 'Product 2',
        'description': 'Description of product 2',
        'price': 15.49
    },
    {
        'id': 3,
        'name': 'Product 3',
        'description': 'Description of product 3',
        'price': 22.75
    }
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:id>')
def product_detail(id):
    product = next((prod for prod in products if prod['id'] == id), None)
    if product is None:
        return redirect(url_for('index'))
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    
    session['cart'].append(product_id)
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    cart_products = [prod for prod in products if prod['id'] in cart_items]
    return render_template('cart.html', products=cart_products)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
