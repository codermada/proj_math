
from flask import render_template

from . import supdomain

@supdomain.route('/')
def index():
    return render_template('supdomain/index.html')