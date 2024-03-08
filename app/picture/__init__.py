
from flask import Blueprint

picture = Blueprint('picture', __name__)

from . import views

