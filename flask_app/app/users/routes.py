#!/usr/bin/env python
from app.extensions import db
from app.models.user import User
from app.users import bp
from flask import render_template

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('users/index.html', users=users)