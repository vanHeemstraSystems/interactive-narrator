#!/usr/bin/env python
from wtforms import Form, BooleanField
from wtforms import StringField, SubmitField, IntegerField, PasswordField, TextAreaField
from wtforms import validators, ValidationError
from wtforms.validators import Length, DataRequired, Email

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    email = StringField('Email Address', [validators.Length(min=6, max=50), Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', [validators.DataRequired()])
    submit = SubmitField("Register")