from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


class CreateChurchServiceForm(FlaskForm):
    name = StringField("Name of Service", validators = [DataRequired()])
    date = DateField("Date of Service", format = '%Y-%m-%d')
    time = TimeField("Time Service Begins", format = '%H.%M')
    submit = SubmitField("Create Service")