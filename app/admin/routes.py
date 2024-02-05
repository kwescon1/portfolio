from flask import render_template,flash,redirect,url_for
from flask_login import login_required,current_user
from app.admin import bp

@bp.route('/')
@login_required
def index():
    email = current_user.email
    return f"logged in {email}"

@login_required
@bp.route('/add-procuct')
def add_product():
    return 'product add page'
