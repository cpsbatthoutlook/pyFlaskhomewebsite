from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, DateField, HiddenField, PasswordField, Form, TextField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, InputRequired

categories=['Apache', 'Bank', 'Brampton', 'Business', 'Canada', 'Car', 'Communication', 'ComputerSales', 'Daddyji', 'Education',
'Efficiency', 'Entertainment', 'Food', 'Finance', 'Government', 'HomeImprovement', 'HTML', 'Java', 'Jojo', 'Linux',
'Meher', 'MQ', 'MicroSoft', 'Music', 'MySQL', 'OpenSource', 'Oracle', 'Others', 'Perl', 'Personal',
'Python', 'RealEstate', 'Rental', 'Research', 'Security', 'Shopping', 'Sol10', 'SysAdmin', 'Tax', 'Virtualization',
'Weblogic', 'Websphere']

class BookmarksForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    # catagory = StringField('Category', validators=[DataRequired()])
    catagory = SelectField('Category', choices=[(c1,c1) for c1 in categories], validators=[DataRequired()] )
    details = StringField('Details', validators=[DataRequired()])
    inserttime = StringField('Insert time', validators=[DataRequired()])
    url = TextField('URL', validators=[DataRequired()])
    submit=SubmitField('Accept')



