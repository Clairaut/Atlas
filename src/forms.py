from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, SubmitField

class EphemerisForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d')
    time = TimeField('Time', format='%H:%M')
    location = StringField('Location')
    submit = SubmitField('Submit')