
from flask import render_template

from . import picture

@picture.route('/')
def index():
    return render_template('picture/index.html')

