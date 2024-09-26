#!/usr/bin/env python
from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    email = db.Column(db.String(150))
    password = db.Column(db.String(150))

    def __repr__(self):
        return f'<User "{self.username}">'