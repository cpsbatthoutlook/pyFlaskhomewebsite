from flask import Blueprint, request, render_template,redirect, url_for, session, flash
from my_app import app,db
from my_app.auth.models import User, RegistrationForm, LoginForm

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/')
@auth_blueprint.route('/home')
def auth_home():
    return render_template('auth_home.html', title=session.get('username','NoUser'))

@auth_blueprint.route('/add2session/<d1>', methods=['GET', 'POST'])
def auth_home2(d1=None):
    # session[d1]=data2
    session['username'] = request.args.get('name', 'Chander1')
    return redirect(url_for('auth.auth_home'))


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def auth_register():
    if session.get('username'):
        return redirect(url_for('auth.auth_home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        existing_username = User.query.filter_by(username = username).first()
        if existing_username:
            return render_template('auth_registration.html', form=form, title='Try Again, user exists!')
        
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.auth_home'))
    if form.errors:
        return "Error submitting form"

    return render_template('auth_registration.html', form=form, title='Register yourself')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def auth_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        existing_username = User.query.filter_by(username = username).first()
        if not( existing_username and existing_username.check_password(password) ):
            return render_template('auth_login.html', form=form, title='Try Again!')
        
        session['username'] = username
        return redirect(url_for('auth.auth_home'))
    if form.errors:
        return "Error submitting form"

    return render_template('auth_login.html', form=form, title='Login yourself')


@auth_blueprint.route('/logout', methods=['GET'])
def auth_logout():
    if session.get('username'):
        session.pop('username')

    return redirect(url_for('auth.auth_home'))