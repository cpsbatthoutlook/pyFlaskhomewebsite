# https://learning-oreilly-com.ezproxy.torontopubliclibrary.ca/library/view/flask-framework-cookbook/9781789951295/72adba2d-b200-46cf-9a6a-ba744eb71fff.xhtml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SECRET_KEY'] = 'c1ecc4ba444d91d97d0da200bdde1da7' 
db = SQLAlchemy(app)

from my_app.catalog.views import catalog_blueprint  #Blueprint
from my_app.hello.views import hello #  Blueprint
from my_app.product.views import product_blueprint #Blueprint
from my_app.auth.views import auth_blueprint #Blueprint

# import my_app.hello.views
# app.register_blueprint(hello)  #  Blueprint for 1st class
# app.register_blueprint(product_blueprint)  # BluePrint for 2nd class
app.register_blueprint(auth_blueprint)

db.create_all()

# Test URLs
# http://127.0.0.1:5000/
# http://127.0.0.1:5000/add/test1/GoodOneTest23
# http://127.0.0.1:5000/show/test1
