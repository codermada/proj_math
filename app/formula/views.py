
from flask import render_template

from . import formula

@formula.route('/')
def index():
    return render_template('formula/index.html')

