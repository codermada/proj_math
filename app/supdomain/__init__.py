
from flask import Blueprint

supdomain = Blueprint('supdomain', __name__)

from . import views

