#!/usr/bin/env python
import sys
import os
import math
import json
import datetime, time

# tell python where to look for packages
sys.path.append('/var/www/interactivenarrator')

from sqlalchemy import create_engine, select, update, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, not_, or_
from slqalchemy.sql import func
from flask import Flask, jsonify, render_template, url_for, request
from flask import flash, send_from_directory, Response, session
from flask_sqlalchemy import SQLAlchemy
# MORE
from markupsafe import escape
import config, socket

# optional, when requiring SQL statements
# from sqlalchemy.sql import func

# tell python where to look for VisualNarrator packages
sys.path.append('/var/www/VisualNarrator')

# from VisualNarrator import run

# preload Spacey NLP
# spacy_nlp = run.initialize_nlp()

# import the database models
# from models import Base

# configuration settings from config.py
app = Flask(__name__)
app.config.from_object(config)

# define a database
db = SQLAlchemy(app)
# db.Model = Base

# MORE

# Models: TO DO - In future move these to models.py

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                        server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'

# MORE

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"