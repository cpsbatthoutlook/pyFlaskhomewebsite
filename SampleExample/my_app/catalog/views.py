from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from my_app import db
from my_app.catalog.models import Product

catalog_blueprint = Blueprint('catalog', __name__)

@catalog_blueprint.route('/')
@catalog_blueprint.route('/home')
def catalog_home():
    return 'Welcome to Catalog home'


@catalog_blueprint.route('/product/<integer: id>')
def catalog_product(id):
    product = Product.query.get_or_404(id)
    return 'Product  - %s, $ %s' % (product.name, product.price)

@catalog_blueprint.route('/products')
def catalog_products():
    products = Product.query.all()
    res = {}
    for product in products:
        res[product:id] = { 'name': product.name, 'price': product.price }
    
    return jsonify(res)

@catalog_blueprint.route('/product-create', methods=['POST',])
def catalog_create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    product = Product(name, price)
    db.session.add(product)
    db.session.commit()
    return '%s product is created ' % (product.name)