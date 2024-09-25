#!/usr/bin/env python
from flask import render_template
from app.register import bp

from app.form import RegistrationForm

@bp.route('/register', methods=['GET', 'POST'])
def do_register():

    form = RegistrationForm(request.form)

    username = form.username.data

    error = 'Sorry, we could not register you.'

    return render_template('register.html', form=form, error=error)