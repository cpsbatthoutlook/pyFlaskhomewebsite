from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, DateField, HiddenField, PasswordField, Form
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired

class Bookmarks(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    details = StringField('Details', validators=[DataRequired()])
    inserttime = DateField('Insert time', validators=[DataRequired()])
    submit=SubmitField('Accept')



