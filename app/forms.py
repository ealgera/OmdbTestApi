from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Required
#from wtforms import validators

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])
    remember_me = BooleanField("Remenber me")
    submit = SubmitField("Sign In")

class SearchForm(FlaskForm):
    search_field = StringField("Zoek naar", validators=[Required()])
    submit = SubmitField("Zoek")
