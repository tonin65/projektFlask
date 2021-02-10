from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('Enter Name')])
    email = StringField('E-mail', validators=[DataRequired('Enter Email'),Email('Enter Email')])
    subject = StringField('Subject', validators=[DataRequired('Enter Title')])
    message = TextAreaField('Message', validators=[DataRequired('Enter Message')])
    submit = SubmitField("Submit")