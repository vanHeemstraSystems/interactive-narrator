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
from flask import Flask, jsonify, render_template, url_for, request
from flask import flash, send_from_directory, Response, session
from flask_sqlalchemy import SQLAlchemy
# MORE
from markupsafe import escape
import config, socket

# optional
from sqlalchemy.sql import func

# tell python where to look for VisualNarrator packages
sys.path.append('/var/www/VisualNarrator')

# from VisualNarrator import run

# preload Spacey NLP
# spacy_nlp = run.initialize_nlp()

# import the database models
# MORE

# configuration settings from config.py
app = Flask(__name__)
app.config.from_object(config)

# MORE

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"