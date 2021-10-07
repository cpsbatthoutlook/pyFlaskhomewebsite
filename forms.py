from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class Knowledgebase(FlaskForm):
    id = IntegerField('ID', validators=[])
    category = StringField('Category', validators=[DataRequired()])
    subcategory = StringField('Sub Category', validators=[DataRequired()])    
    subject = StringField('Subject', validators=[DataRequired()])    
    description = StringField('Description', validators=[DataRequired()])    
    inserttime = DateTimeField('Insert Time')
    submit = SubmitField('Add')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password  = PasswordField('Password', validators=[DataRequired()])
    confirm_password  = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
class LoginForm(FlaskForm):
    email = StringField('Login id', validators=[DataRequired(), Email()])
    password  = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
