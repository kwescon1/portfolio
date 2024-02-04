from flask import Blueprint

bp = Blueprint('admin', __name__)


# import routes file

from app.admin import routes

