#!/usr/bin/env python
from app.extensions import db
from datetime import datetime
# from sqlalchemy import Column, Table, DateTime, Boolean, String

class User(db.Model):
    """A user login, with credentials and authentication."""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.now)
    modified = db.Column(db.DateTime, default=datetime.now,
                      onupdate=datetime.now)    
    username = db.Column('username', db.String(200))
    email = db.Column(db.String(100), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True)
    password = db.Column('password', db.String(100))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    def __repr__(self):
        return f'<User "{self.username}">'