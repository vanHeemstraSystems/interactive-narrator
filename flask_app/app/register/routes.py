#!/usr/bin/env python
from flask import render_template, request
from app.register import bp

from app.form import RegistrationForm

@bp.route('/register', methods=['GET', 'POST'])
def do_register():
  try:
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        print('validating was a success')

        username = form.username.data

    else:
      return render_template("register.html", form=form)

  except Exception as e:
    print('an exception occured', e)

    error = 'Sorry, we could not register you.'

    return render_template('register.html', form=form, error=error)