#!/usr/bin/env python
from wtforms import Form, BooleanField

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])