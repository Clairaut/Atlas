from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, TimeField, SubmitField

class EphemerisForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d')
    time = TimeField('Time', format='%H:%M')
    location = StringField('Location')
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    confirm = PasswordField('Confirm')
    submit = SubmitField('Submit')