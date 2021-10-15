#from werkzeug.exceptions import abort
from flask import render_template, redirect, url_for
from flask import Blueprint
from my_app.product.models import PRODUCTS

product_blueprint=Blueprint('product', __name__)

@product_blueprint.route('/')
@product_blueprint.route('/home')
def product_home():
    return render_template('home_product.html', products=PRODUCTS)


@product_blueprint.route('/product/<key>')
def product(key):
    product = PRODUCTS.get(key)
    if not product:
        # abort(404)
        return "Error"
    return render_template('product.html', product=product)