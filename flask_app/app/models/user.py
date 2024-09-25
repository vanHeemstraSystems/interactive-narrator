#!/usr/bin/env python
from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<User "{self.username}">'