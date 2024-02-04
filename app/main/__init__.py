from flask import Blueprint

bp = Blueprint('main', __name__)


# import routes file

from app.main import routes

