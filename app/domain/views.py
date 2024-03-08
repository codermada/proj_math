
from flask import render_template

from . import domain

@domain.route('/')
def index():
    return render_template('domain/index.html')

