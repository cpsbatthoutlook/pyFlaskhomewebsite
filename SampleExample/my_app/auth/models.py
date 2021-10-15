from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, EqualTo
from my_app import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    pwdhash = db.Column(db.String())

    def  __init__(self, username, password):
        self.username = username
        self.pwdhash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    ##Flask based Authentication 
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    # @property : to remove TypeError: 'str' object is not callable issue
    def get_id(self):
        return str(self.id)
        # return self.id
    
    ##Flask based Authentication  finished

class RegistrationForm(FlaskForm):
    username = TextField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords mush match')])
    confirm = PasswordField('Confirm Password',validators= [InputRequired()])

class LoginForm(FlaskForm):
    username = TextField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


