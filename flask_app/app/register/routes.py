#!/usr/bin/env python
import os
import sys

from app import sqlsession
from app.form import RegistrationForm
from app.extensions import db
from app.models.user import User
from app.register import bp
from flask import render_template, request
from passlib.hash import sha256_crypt

@bp.route('/register', methods=['GET', 'POST'])
def do_register():
  try:
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        print('validating was a success')
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt((str(form.password.data)))
        # check by username if a user is new or existent...
        user_exists = sqlsession.query(User).filter(User.username == username).first()
        # ... if it exists, notify the user
        if user_exists:
          error = "That username is already taken, please choose another."
          return render_template('register.html', form=form, error=error)
        # ..else, create the new user
        else:
          print('success, user does not exist yet')
          new_user = User(username=username, email=email, password=password)
          sqlsession.add(new_user)
          sqlsession.commit()
          welcome_text = 'Hi, you created an account with Interactive Narrator.'
          send_email('Your account with Interactive Narrator', email, welcome_text)
          session['logged_in'] = True
          session['username'] = username
          if session['username'] == 'admin':
            return redirect(url_for('admin_dashboard'))
          else:
            return redirect(url_for('show_dash'))  
    else:
      return render_template("register.html", form=form)

  except Exception as e:
    print('an exception occured', e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    # make sure the session is reverted if an error occured
    sqlsession.rollback()
    error = 'Sorry, we could not register you.'
    return render_template('register.html', form=form, error=error)