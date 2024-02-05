from flask import render_template,flash,redirect,url_for
from app.services.forms import LoginForm
from app.admin import bp





@bp.route('/')
def index():
    return "logged in"

@bp.route('/add-procuct')
def add_product():
    return 'product add page'
