#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint('register', __name__)

from app.register import routes