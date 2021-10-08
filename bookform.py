from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, DateField, HiddenField, PasswordField, Form
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired

class BookmarksForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    catagory = StringField('Category', validators=[DataRequired()])
    details = StringField('Details', validators=[DataRequired()])
    inserttime = DateField('Insert time', validators=[DataRequired()])
    url = StringField('URL', validators=[DataRequired()])
    submit=SubmitField('Accept')



