# from my_app import app
from flask import Blueprint  #BluePrint
from flask import render_template, request, redirect, url_for

from my_app.hello.models import MESSAGES

hello = Blueprint('hello', __name__) #BluePrint

# @app.route('/')
# @app.route('/hello')
@hello.route('/hello')
def hello_world():
    return MESSAGES['default']

# @app.route('/show/<key>')
@hello.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key

@hello.route('/add/<key>/<message>')
# @app.route('/add/<key>/<message>')
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Added/Updated" % key

@hello.route('/insideview/<user>')
def hello_world1(user=None):
    user = user or 'Chander'
    return '''<html> 
    <head> 
      <title>Flask Framework Cookbook</title> 
 
    </head> 
      <body> 
        <h1>Hello %s!</h1> 
        <p>Welcome to the world of Flask!</p> 
      </body> 
</html     ''' % user

@hello.route('/hello3')
def hello3():
    user = request.args.get('user', 'Chander')
    return render_template('hello_index.html', user=user)