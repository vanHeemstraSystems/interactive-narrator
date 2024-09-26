#!/usr/bin/env python
from flask import render_template
from app.users import bp
from app.extensions import db
from app.models.user import User

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('users/index.html', users=users)