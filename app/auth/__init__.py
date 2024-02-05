from flask import Blueprint

bp = Blueprint('auth', __name__)


# import routes file

from app.auth import routes

