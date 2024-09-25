#!/usr/bin/env python
from wtforms import Form, BooleanField
from wtforms import StringField, SubmitField, IntegerField, PasswordField, TextAreaField
from wtforms import validators, ValidationError
from wtforms.validators import Length, DataRequired, Email

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])