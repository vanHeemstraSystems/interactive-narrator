#!/usr/bin/env python
from flask import Blueprint

bp = Blueprint('users', __name__)

from app.users import routes