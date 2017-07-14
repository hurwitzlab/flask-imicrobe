from flask import Blueprint


imicrobe = Blueprint('imicrobe', __name__)

from . import projects
