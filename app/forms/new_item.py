from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo

class ItemForm(FlaskForm):
    website_name = StringField('Website Name',validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password',validators = [DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Save Password')

