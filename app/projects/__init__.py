from flask import Blueprint

bp = Blueprint('projects', __name__)


# import routes file

from app.projects import routes

