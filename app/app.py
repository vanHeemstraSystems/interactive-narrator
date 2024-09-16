#!/usr/bin/env python
import sys
import os
import math
import json
import datetime, time

# tell python where to look for packages
# sys.path.append('/var/www/interactivenarrator')

from flask import Flask, jsonify, render_template, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"